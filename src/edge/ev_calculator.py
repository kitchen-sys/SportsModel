from __future__ import annotations

from dataclasses import dataclass
from typing import List

from models.distribution import american_to_decimal, american_to_probability


@dataclass
class ExpectedValueResult:
    expected_value: float
    true_prob: float
    market_prob: float


def compute_expected_value(true_prob: float, odds: int) -> ExpectedValueResult:
    market_prob = american_to_probability(odds)
    payout = american_to_decimal(odds) - 1
    ev = true_prob * payout - market_prob
    return ExpectedValueResult(expected_value=ev, true_prob=true_prob, market_prob=market_prob)


__all__: List[str] = ["ExpectedValueResult", "compute_expected_value"]
