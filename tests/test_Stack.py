from contextlib import nullcontext as does_not_raise

import pytest

from src.Stack import Stack


@pytest.mark.parametrize(
    "start_stack, add_val, res_len, expectation",
    [
        ([1, 2, 3], 4, 4, does_not_raise()),
        ([], 1, 1, does_not_raise()),
    ]
)
def test_push(start_stack, add_val, res_len, expectation):
    with expectation:
        stack = Stack(start_stack)
        
        stack.push(add_val)
        assert len(stack) == res_len
        assert stack.arr[-1] == add_val


@pytest.mark.parametrize(
    "start_stack, res_val, res_len, expectation",
    [
        ([1, 2, 3], 3, 2, does_not_raise()),
        ([1], 1, 0, does_not_raise()),
        ([], None, None, pytest.raises(IndexError))
    ]
)
def test_pop(start_stack, res_val, res_len, expectation):
    with expectation:
        stack = Stack(start_stack)
        
        popped = stack.pop()
        assert popped == res_val
        assert len(stack) == res_len


@pytest.mark.parametrize(
    "start_stack, res_val, expectation",
    [
        ([1, 2, 3], 3, does_not_raise()),
        ([1], 1, does_not_raise()),
        ([], None, pytest.raises(IndexError))
    ]
)
def test_peek(start_stack, res_val, expectation):
    with expectation:
        stack = Stack(start_stack)
        
        top = stack.peek()
        assert top == res_val


@pytest.mark.parametrize(
    "start_stack, res, expectation",
    [
        ([1, 2, 3], False, does_not_raise()),
        ([], True, does_not_raise())
    ]
)
def test_is_empty(start_stack, res, expectation):
    with expectation:
        stack = Stack(start_stack)
        
        empty = stack.is_empty()
        assert empty == res


@pytest.mark.parametrize(
    "start_stack, res_val, expectation",
    [
        ([3, 2, 1], 1, does_not_raise()),
        ([5, 5, 5], 5, does_not_raise()),
        ([], None, pytest.raises(IndexError))
    ]
)
def test_min(start_stack, res_val, expectation):
    with expectation:
        stack = Stack(start_stack)
        
        min_val = stack.min()
        assert min_val == res_val


@pytest.mark.parametrize(
    "start_stack, res_len, expectation",
    [
        ([1, 2, 3], 3, does_not_raise()),
        ([], 0, does_not_raise())
    ]
)
def test_len(start_stack, res_len, expectation):
    with expectation:
        stack = Stack(start_stack)
        
        length = len(stack)
        assert length == res_len