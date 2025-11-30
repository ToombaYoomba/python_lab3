from contextlib import nullcontext as does_not_raise

import pytest

from src.fact_fibo.factorial import factorial


@pytest.mark.parametrize(
    "res, ans, expectation",
    [
        (factorial(0), 1, does_not_raise()),
        (factorial(10), 3628800, does_not_raise()),
        (factorial(42), 1405006117752879898543142606244511569936384000000000, does_not_raise()),
    ],
)
def test_factorial(res, ans, expectation):
    with expectation:
        assert res == ans
