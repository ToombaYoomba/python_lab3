from src.compare_items import compare_items
from typing import TypeVar, Callable, Any

def bubble_sort(a: list[int], key_custom: Callable[[TypeVar], Any] | None = None,
                 cmp_custom: Callable[[TypeVar, TypeVar], int] | None = None) -> list[int]:
    '''
    Получает массив целых чисел и функции для ключа и компаратора

    Сортирует массив пузырьковой сортировкой, каждый раз поднимая самое большое число вверх массива
    Учитывает ключ и компаратор при сортировке. Ключ отвечает за то, что сравнивается в числа, а компаратор за то, как сортируются числа

    Возвращает отсортированный массив
    '''
    N: int = len(a)

    for i in range(N - 1):
        for j in range(N - i - 1):
            if compare_items(a[j], a[j+1], key_custom, cmp_custom) == 1:
                a[j], a[j+1] = a[j+1], a[j]
            # print(a)

    return a

# print(bubble_sort(list(map(int, input().split())), key_custom=abs, cmp_custom = lambda a, b: b - a))
# print(bubble_sort(list(map(int, input().split()))))