import pytest

from defi_liquidity_pool_simulation import quote_constant_product_swap


def test_quote_matches_fee_adjusted_constant_product_formula() -> None:
    quote = quote_constant_product_swap(1_000_000, 2_000_000, 1_000, 0.003)

    expected = 2_000_000 * (1_000 * (1 - 0.003)) / (
        1_000_000 + 1_000 * (1 - 0.003)
    )
    assert quote.amount_out == pytest.approx(expected)
    assert quote.fee_amount == pytest.approx(3)
    assert quote.spot_price == pytest.approx(2)
    assert quote.execution_price == pytest.approx(expected / 1_000)
    assert 0 < quote.price_impact < 1


def test_zero_fee_quote_uses_full_input_in_formula() -> None:
    quote = quote_constant_product_swap(1_000, 2_000, 100, 0)
    assert quote.amount_out == pytest.approx(2_000 * 100 / 1_100)
    assert quote.fee_amount == 0


@pytest.mark.parametrize(
    ("reserve_in", "reserve_out", "amount_in", "fee_rate"),
    [
        (0, 100, 1, 0.003),
        (100, -1, 1, 0.003),
        (100, 100, 0, 0.003),
        (100, 100, 1, -0.1),
        (100, 100, 1, 1),
    ],
)
def test_invalid_inputs_are_rejected(
    reserve_in: float, reserve_out: float, amount_in: float, fee_rate: float
) -> None:
    with pytest.raises(ValueError):
        quote_constant_product_swap(reserve_in, reserve_out, amount_in, fee_rate)
