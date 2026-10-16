"""CONSORCIO analytical cost calculator.

ID: CONSORCIO-CODE-CUSTO-001
Version: 1.0.0
Phase: G3 — controlled construction
Status: EM_REVISAO
Authority: CONSORCIO G2 baseline and GOVERNANCA repository
Scope: deterministic calculations only; no transactions, real bids, or personal data.
"""
from __future__ import annotations

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from typing import Any


CENT = Decimal("0.01")


def _decimal(value: Any, field: str, *, nullable: bool = False) -> Decimal | None:
    if value is None and nullable:
        return None
    if isinstance(value, bool):
        raise ValueError(f"{field} must be a numeric value, not bool")
    try:
        result = Decimal(str(value))
    except (InvalidOperation, ValueError, TypeError):
        raise ValueError(f"{field} must be numeric") from None
    if not result.is_finite():
        raise ValueError(f"{field} must be finite")
    return result


def _non_negative(value: Any, field: str, *, nullable: bool = False) -> Decimal | None:
    result = _decimal(value, field, nullable=nullable)
    if result is not None and result < 0:
        raise ValueError(f"{field} must be >= 0")
    return result


def calculate_costs(
    *,
    credit_amount: Any,
    installment_count: Any,
    administration_fee_rate_total: Any = None,
    reserve_fund_rate_total: Any = None,
    insurance_total: Any = None,
    other_charges_total: Any = None,
    entry_or_bid_scenario: Any = None,
) -> dict[str, Any]:
    """Return reproducible cost estimates; unknown inputs are never silently zeroed."""
    credit = _decimal(credit_amount, "credit_amount")
    if credit <= 0:
        raise ValueError("credit_amount must be > 0")

    if isinstance(installment_count, bool) or not isinstance(installment_count, int):
        raise ValueError("installment_count must be an integer")
    if installment_count < 1:
        raise ValueError("installment_count must be >= 1")

    admin_rate = _decimal(administration_fee_rate_total, "administration_fee_rate_total", nullable=True)
    reserve_rate = _decimal(reserve_fund_rate_total, "reserve_fund_rate_total", nullable=True)
    for name, rate in (
        ("administration_fee_rate_total", admin_rate),
        ("reserve_fund_rate_total", reserve_rate),
    ):
        if rate is not None and not Decimal("0") <= rate <= Decimal("1"):
            raise ValueError(f"{name} must be between 0 and 1")

    insurance = _non_negative(insurance_total, "insurance_total", nullable=True)
    other = _non_negative(other_charges_total, "other_charges_total", nullable=True)
    bid = _non_negative(entry_or_bid_scenario, "entry_or_bid_scenario", nullable=True)

    administration_fee = credit * admin_rate if admin_rate is not None else None
    reserve_fund = credit * reserve_rate if reserve_rate is not None else None
    components = {
        "administration_fee": administration_fee,
        "reserve_fund": reserve_fund,
        "insurance": insurance,
        "other_charges": other,
    }
    unknown = [name for name, value in components.items() if value is None]
    known_charges = sum((value for value in components.values() if value is not None), Decimal("0"))
    known_subtotal = credit + known_charges
    complete_total = known_subtotal if not unknown else None
    known_extra_charges = known_charges
    fee_percentage = (known_extra_charges / credit * Decimal("100")) if not unknown else None

    money = lambda value: str(value.quantize(CENT, rounding=ROUND_HALF_UP)) if value is not None else None
    return {
        "currency": "BRL",
        "credit_amount": money(credit),
        "administration_fee": money(administration_fee),
        "reserve_fund": money(reserve_fund),
        "insurance_total": money(insurance),
        "other_charges_total": money(other),
        "known_cost_subtotal": money(known_subtotal),
        "complete_total_cost": money(complete_total),
        "average_installment": money(complete_total / installment_count) if complete_total is not None else None,
        "known_extra_charges": money(known_extra_charges),
        "known_extra_charges_pct": str(fee_percentage.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)) if fee_percentage is not None else None,
        "installment_count": installment_count,
        "entry_or_bid_scenario": money(bid),
        "unknown_components": unknown,
        "note": "Entry/bid scenario is informational only and is not included in contractual cost.",
    }


def project_adjustment_scenario(*, base_total_cost: Any, period_rates: list[Any], installment_count: Any) -> dict[str, Any]:
    """Project explicit hypothetical rates; this is sensitivity analysis, not a contract forecast."""
    base = _decimal(base_total_cost, "base_total_cost")
    if base <= 0:
        raise ValueError("base_total_cost must be > 0")
    if isinstance(installment_count, bool) or not isinstance(installment_count, int) or installment_count < 1:
        raise ValueError("installment_count must be a positive integer")
    if not isinstance(period_rates, list) or not period_rates:
        raise ValueError("period_rates must be a non-empty list")
    current = base
    steps = []
    for index, raw_rate in enumerate(period_rates, start=1):
        rate = _decimal(raw_rate, f"period_rates[{index - 1}]")
        if rate <= Decimal("-1"):
            raise ValueError(f"period_rates[{index - 1}] must be > -1")
        current *= Decimal("1") + rate
        steps.append({"period": index, "rate": str(rate), "projected_total": str(current.quantize(CENT, rounding=ROUND_HALF_UP))})
    money = lambda value: str(value.quantize(CENT, rounding=ROUND_HALF_UP))
    return {
        "scenario_type": "SENSITIVITY_ONLY",
        "currency": "BRL",
        "base_total_cost": money(base),
        "period_count": len(period_rates),
        "periods": steps,
        "projected_total_cost": money(current),
        "average_installment": money(current / installment_count),
        "installment_count": installment_count,
        "assumption": "Each explicit rate is compounded on the full base total once per period; this is not a contract forecast.",
    }
