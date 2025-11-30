from contextlib import nullcontext as does_not_raise

import pytest

from src.fact_fibo.fibo import fibo


@pytest.mark.parametrize(
        "res, ans, expectation",
        [
            (fibo(1), 1, does_not_raise()),
            (fibo(10), 55, does_not_raise()),
            (fibo(42), 267914296, does_not_raise())
        ]
)
def test_fibo(res, ans, expectation):
    with expectation:
        assert res == ans