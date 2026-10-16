"""Structural contract checks for the CONSORCIO JSON Schema.

These tests inspect the schema definition; they are not a full JSON Schema validator.
"""
import json
import unittest
from pathlib import Path


SCHEMA_PATH = Path(__file__).parents[1] / "DADOS" / "esquemas" / "consorcio-custo.schema.json"


class CostSchemaContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))

    def test_schema_uses_2020_12_and_rejects_unknown_top_level_fields(self):
        self.assertEqual(self.schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
        self.assertFalse(self.schema["additionalProperties"])

    def test_required_base_fields_are_present(self):
        self.assertTrue({
            "scenario_id", "currency", "credit_amount", "installment_count",
            "source_classification", "as_of_date", "fees",
        }.issubset(set(self.schema["required"])))

    def test_fact_and_hypothesis_have_conditional_provenance_rules(self):
        conditions = self.schema["allOf"]
        self.assertEqual(len(conditions), 2)
        fact = next(item for item in conditions if item["if"]["properties"]["source_classification"]["const"] == "FACTO")
        hypothesis = next(item for item in conditions if item["if"]["properties"]["source_classification"]["const"] == "HIPOTESE")
        self.assertIn("source_reference", fact["then"]["required"])
        self.assertIn("source_observed_at", fact["then"]["required"])
        self.assertIn("assumptions", hypothesis["then"]["required"])

    def test_adjustment_scenario_requires_explicit_period_rates(self):
        scenario = self.schema["properties"]["adjustment_scenario"]
        self.assertIn("period_rates", scenario["required"])
        self.assertGreater(scenario["properties"]["period_rates"]["minItems"], 0)
        self.assertEqual(scenario["properties"]["application_basis"]["const"], "TOTAL_KNOWN_COST")


if __name__ == "__main__":
    unittest.main()
