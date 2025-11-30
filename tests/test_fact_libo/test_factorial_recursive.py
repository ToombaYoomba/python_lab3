from contextlib import nullcontext as does_not_raise

import pytest

from src.fact_fibo.factorial_recursive import factorial_recursive


@pytest.mark.parametrize(
    "res, ans, expectation",
    [
        (factorial_recursive(0), 1, does_not_raise()),
        (factorial_recursive(10), 3628800, does_not_raise()),
        # (factorial_recursive(42), 1405006117752879898543142606244511569936384000000000, does_not_raise()),
    ],
)
def test_factorial_recursive(res, ans, expectation):
    with expectation:
        assert res == ans