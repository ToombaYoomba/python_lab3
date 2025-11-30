from contextlib import nullcontext as does_not_raise

import pytest

from src.sort_methods.heap_sort import heap_sort


@pytest.mark.parametrize(
    "inp, expectation",
    [
        ([1, 2, 3, 4, 5], does_not_raise()),
        ([5, 4, 3, 2, 1], does_not_raise()),
        ([3, 1, 4, 2, 5], does_not_raise()),
        ([2, 5, 2, 1, 5], does_not_raise()),
        ([-2, 0, 3, -5, 1], does_not_raise()),
        ([7, 7, 7, 7], does_not_raise()),
        ([], does_not_raise()),
        ([42], does_not_raise()),
    ],
)
def test_heap_sort(inp, expectation):
    with expectation:
        assert heap_sort(inp) == sorted(inp)