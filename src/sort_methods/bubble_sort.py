from src.compare_items import compare_items
from typing import TypeVar, Callable, Any

def bubble_sort(a: list[int], key_custom: Callable[[TypeVar], Any] | None = None,
                 cmp_custom: Callable[[TypeVar, TypeVar], int] | None = None) -> list[int]:
    N: int = len(a)

    for i in range(N - 1):
        for j in range(N - i - 1):
            if compare_items(a[j], a[j+1], key_custom, cmp_custom) == 1:
                a[j], a[j+1] = a[j+1], a[j]
            # print(a)

    return a

# print(bubble_sort(list(map(int, input().split())), cmp_custom = lambda a, b: b - a))
# print(bubble_sort(list(map(int, input().split()))))