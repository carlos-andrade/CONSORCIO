"""Unit tests for the CONSORCIO deterministic cost calculator."""
import unittest
from decimal import Decimal

from MODELOS.custos.calculadora_custos import calculate_costs


class CostCalculatorTests(unittest.TestCase):
    def test_reference_case(self):
        result = calculate_costs(
            credit_amount=100000,
            administration_fee_rate_total="0.15",
            reserve_fund_rate_total="0.02",
            insurance_total=1200,
            other_charges_total=300,
            installment_count=100,
        )
        self.assertEqual(result["administration_fee"], "15000.00")
        self.assertEqual(result["reserve_fund"], "2000.00")
        self.assertEqual(result["complete_total_cost"], "118500.00")
        self.assertEqual(result["average_installment"], "1185.00")
        self.assertEqual(result["known_extra_charges"], "18500.00")
        self.assertEqual(result["known_extra_charges_pct"], "18.50")
        self.assertEqual(result["unknown_components"], [])

    def test_rejects_zero_credit(self):
        with self.assertRaisesRegex(ValueError, "credit_amount must be > 0"):
            calculate_costs(credit_amount=0, installment_count=10)

    def test_rejects_non_integer_or_zero_installments(self):
        for count in (0, 2.5, True):
            with self.subTest(count=count), self.assertRaises(ValueError):
                calculate_costs(credit_amount=100, installment_count=count)

    def test_rejects_fee_rates_outside_range(self):
        for rate in ("-0.01", "1.01"):
            with self.subTest(rate=rate), self.assertRaises(ValueError):
                calculate_costs(
                    credit_amount=100, installment_count=10,
                    administration_fee_rate_total=rate,
                )

    def test_rejects_negative_reserve_rate(self):
        with self.assertRaisesRegex(ValueError, "reserve_fund_rate_total"):
            calculate_costs(
                credit_amount=100, installment_count=10,
                reserve_fund_rate_total="-0.1",
            )

    def test_unknown_components_are_not_silently_zeroed(self):
        result = calculate_costs(credit_amount=1000, installment_count=10)
        self.assertIsNone(result["complete_total_cost"])
        self.assertIsNone(result["average_installment"])
        self.assertEqual(
            result["unknown_components"],
            ["administration_fee", "reserve_fund", "insurance", "other_charges"],
        )
        self.assertEqual(result["known_cost_subtotal"], "1000.00")

    def test_rejects_negative_other_charges(self):
        with self.assertRaisesRegex(ValueError, "other_charges_total must be >= 0"):
            calculate_costs(
                credit_amount=100, installment_count=10,
                other_charges_total=-1,
            )

    def test_bid_scenario_is_separate_from_cost(self):
        result = calculate_costs(
            credit_amount=1000, installment_count=10,
            administration_fee_rate_total="0.1",
            reserve_fund_rate_total="0.02",
            insurance_total=0, other_charges_total=0,
            entry_or_bid_scenario=250,
        )
        self.assertEqual(result["complete_total_cost"], "1120.00")
        self.assertEqual(result["entry_or_bid_scenario"], "250.00")

    def test_rejects_non_finite_values(self):
        with self.assertRaises(ValueError):
            calculate_costs(credit_amount="NaN", installment_count=10)


    def test_adjustment_scenario_compounds_explicit_rates(self):
        from MODELOS.custos.calculadora_custos import project_adjustment_scenario
        result = project_adjustment_scenario(base_total_cost=1000, period_rates=["0.10", "0.05"], installment_count=10)
        self.assertEqual(result["periods"][0]["projected_total"], "1100.00")
        self.assertEqual(result["periods"][1]["projected_total"], "1155.00")
        self.assertEqual(result["projected_total_cost"], "1155.00")
        self.assertEqual(result["average_installment"], "115.50")
        self.assertEqual(result["scenario_type"], "SENSITIVITY_ONLY")

    def test_adjustment_scenario_rejects_rate_at_or_below_minus_one(self):
        from MODELOS.custos.calculadora_custos import project_adjustment_scenario
        for rate in ("-1", "-1.01"):
            with self.subTest(rate=rate), self.assertRaises(ValueError):
                project_adjustment_scenario(base_total_cost=1000, period_rates=[rate], installment_count=10)

    def test_adjustment_scenario_requires_nonempty_rates(self):
        from MODELOS.custos.calculadora_custos import project_adjustment_scenario
        with self.assertRaises(ValueError):
            project_adjustment_scenario(base_total_cost=1000, period_rates=[], installment_count=10)


    def test_comparison_ranks_only_equivalent_complete_scenarios(self):
        from MODELOS.custos.calculadora_custos import compare_cost_scenarios
        common = {
            "as_of_date": "2026-10-16", "source_classification": "SINTETICO",
            "credit_amount": 100000, "installment_count": 100,
            "reserve_fund_rate_total": "0.02", "insurance_total": 1000,
            "other_charges_total": 0,
        }
        result = compare_cost_scenarios(scenarios=[
            {**common, "scenario_id": "PLANO-B", "administration_fee_rate_total": "0.15"},
            {**common, "scenario_id": "PLANO-A", "administration_fee_rate_total": "0.10"},
        ])
        self.assertEqual(result["comparison_status"], "COMPARABLE")
        self.assertEqual([x["scenario_id"] for x in result["ranking"]], ["PLANO-A", "PLANO-B"])
        self.assertEqual([x["rank"] for x in result["ranking"]], [1, 2])

    def test_comparison_rejects_different_credit_or_term(self):
        from MODELOS.custos.calculadora_custos import compare_cost_scenarios
        base = {
            "scenario_id": "A", "as_of_date": "2026-10-16",
            "source_classification": "SINTETICO", "credit_amount": 1000,
            "installment_count": 10, "administration_fee_rate_total": "0.1",
            "reserve_fund_rate_total": "0.02", "insurance_total": 0, "other_charges_total": 0,
        }
        for change in ({"credit_amount": 2000}, {"installment_count": 20}):
            with self.subTest(change=change), self.assertRaisesRegex(ValueError, "not comparable"):
                compare_cost_scenarios(scenarios=[base, {**base, "scenario_id": "B", **change}])

    def test_comparison_blocks_unknown_cost_components(self):
        from MODELOS.custos.calculadora_custos import compare_cost_scenarios
        base = {
            "as_of_date": "2026-10-16", "source_classification": "SINTETICO",
            "credit_amount": 1000, "installment_count": 10,
            "administration_fee_rate_total": "0.1", "reserve_fund_rate_total": "0.02",
            "insurance_total": None, "other_charges_total": 0,
        }
        with self.assertRaisesRegex(ValueError, "unknown material cost components"):
            compare_cost_scenarios(scenarios=[
                {**base, "scenario_id": "A"},
                {**base, "scenario_id": "B", "insurance_total": 0},
            ])


if __name__ == "__main__":
    unittest.main()
