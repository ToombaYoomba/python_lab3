from contextlib import nullcontext as does_not_raise

import pytest

from src.sort_methods.bucket_sort import bucket_sort


@pytest.mark.parametrize(
    "inp, expectation",
    [
        ([0.1, 0.5, 0.3, 0.9, 0.2], does_not_raise()),
        ([0.01, 0.02, 0.015, 0.019, 0.011], does_not_raise()),
        ([0.001, 0.5, 0.999, 0.1, 0.8], does_not_raise()),
    ],
)
def test_bucket_sort(inp, expectation):
    with expectation:
        assert bucket_sort(inp) == sorted(inp)