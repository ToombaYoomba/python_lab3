from random import choice
from typing import TypeVar, Callable, Any
from src.compare_items import compare_items

def quick_sort(a: list[int], key_custom: Callable[[TypeVar], Any] | None = None,
                 cmp_custom: Callable[[TypeVar, TypeVar], int] | None = None) -> list[int]:
    if len(a) <= 1:
        return a
     
    else:
        pick: int = choice(a)
        print("pick", pick)
        left: list[int] = []
        middle: list[int] = []
        right: list[int] = []
        for e in a:
            if compare_items(e, pick, key_custom, cmp_custom) == -1:
                left.append(e)
                # print("left", left)
            elif compare_items(e, pick, key_custom, cmp_custom) == 0:
                middle.append(e)
                # print("middle", middle)
            else:
                right.append(e)
                # print("right", right)
        
        print(left, middle, right)
        
        return quick_sort(left, key_custom, cmp_custom) + middle + quick_sort(right, key_custom, cmp_custom)
    
# print(quick_sort(list(map(int, input().split())), cmp_custom = lambda a, b: b - a))