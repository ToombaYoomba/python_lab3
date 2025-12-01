from contextlib import nullcontext as does_not_raise
from functools import cmp_to_key

import pytest

from src.sort_methods.bubble_sort import bubble_sort


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
def test_bubble_sort(inp, expectation):
    with expectation:
        assert bubble_sort(inp) == sorted(inp)

@pytest.mark.parametrize(
    "inp, key_custom, cmp_custom, expectation",
    [
        ([-5, 2, -1, 4, -3], eval("abs"), None, does_not_raise()),
        ([5, 1, 3, 2, 4], eval("lambda x: -x"), None, does_not_raise()),
        ([7, 5, 8, 2, 4], eval("lambda x: x % 3"), None, does_not_raise()),
        
        ([5, 1, 3, 2, 4], None, eval("lambda a, b: a - b"), does_not_raise()),
        ([1, 2, 3, 4, 5], None, eval("lambda a, b: b - a"), does_not_raise()),

        ([-5, 2, -1, 4, -3], eval("abs"), eval("lambda a, b: b - a"), does_not_raise()),
    ],
)
def test_bubble_sort_key_cmp(inp, key_custom, cmp_custom, expectation):
    with expectation:
        result = bubble_sort(inp, key_custom=key_custom, cmp_custom=cmp_custom)

        if key_custom is not None and cmp_custom is None:
            expected = sorted(inp, key=key_custom)
        elif cmp_custom is not None and key_custom is None:
            expected = sorted(inp, key=cmp_to_key(cmp_custom))
        else:
            expected = sorted(inp, key=abs, reverse=True)
            
        assert result == expected