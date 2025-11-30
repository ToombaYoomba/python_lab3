from contextlib import nullcontext as does_not_raise

import pytest

from src.fact_fibo.fibo_recursive import fibo_recursive


@pytest.mark.parametrize(
    "res, ans, expectation",
    [
        (fibo_recursive(1), 1, does_not_raise()),
        (fibo_recursive(10), 55, does_not_raise()),
        # (fibo_recursive(42), 267914296, does_not_raise()),
    ],
)
def test_fibo_recursive(res, ans, expectation):
    with expectation:
        assert res == ans
