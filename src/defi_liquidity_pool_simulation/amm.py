"""Pure constant-product AMM calculations used by the course baseline."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SwapQuote:
    """Quote for one swap; prices use output-token units per input-token unit."""

    amount_in: float
    amount_out: float
    fee_amount: float
    spot_price: float
    execution_price: float
    price_impact: float


def quote_constant_product_swap(
    reserve_in: float,
    reserve_out: float,
    amount_in: float,
    fee_rate: float = 0.003,
) -> SwapQuote:
    """Return a fee-inclusive quote for x*y=k without mutating pool reserves.

    The gross input enters the pool. The fee is retained in reserves, while
    only the fee-adjusted input is used in the constant-product output formula.
    Price impact is measured against the pre-trade spot price and includes fees.
    """
    if reserve_in <= 0 or reserve_out <= 0:
        raise ValueError("reserves must be positive")
    if amount_in <= 0:
        raise ValueError("amount_in must be positive")
    if not 0 <= fee_rate < 1:
        raise ValueError("fee_rate must be in [0, 1)")

    fee_amount = amount_in * fee_rate
    effective_input = amount_in - fee_amount
    amount_out = reserve_out * effective_input / (reserve_in + effective_input)
    spot_price = reserve_out / reserve_in
    execution_price = amount_out / amount_in
    price_impact = 1 - execution_price / spot_price
    return SwapQuote(
        amount_in=amount_in,
        amount_out=amount_out,
        fee_amount=fee_amount,
        spot_price=spot_price,
        execution_price=execution_price,
        price_impact=price_impact,
    )
