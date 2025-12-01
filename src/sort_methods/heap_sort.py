from src.compare_items import compare_items
from typing import TypeVar, Callable, Any

def heapi(a: list[int], n: int, i: int, key_custom: Callable[[TypeVar], Any] | None = None,
                 cmp_custom: Callable[[TypeVar, TypeVar], int] | None = None) -> None:
    '''
    Получает массив целых чисел и функции для ключа и компаратора

    Сортирует массив, создавая дерево чисел
    Каждый раз делает верное дерево, в котором у родительского элемента значение больше, чем у дочернего
    Потом достаёт верхний элемент дерева и перемещает его вверх списка
    Повторяет, пока дерево не кончится
    Учитывает ключ и компаратор при сортировке. Ключ отвечает за то, что сравнивается в числа, а компаратор за то, как сортируются числа
    
    Возвращает отсортированный массив
    '''
    largest: int = i
    left: int = 2 * i + 1
    right: int = 2 * i + 2

    if left < n and compare_items(a[left], a[largest], key_custom, cmp_custom) == 1:
        largest = left

    if right < n and compare_items(a[right], a[largest], key_custom, cmp_custom) == 1:
        largest = right

    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapi(a, n, largest, key_custom, cmp_custom)

def heap_sort(a: list[int], key_custom: Callable[[TypeVar], Any] | None = None,
                 cmp_custom: Callable[[TypeVar, TypeVar], int] | None = None) -> list[int]:
    a: list[int] = a.copy()
    n: int = len(a)
    
    for i in range(n // 2 - 1, -1, -1):
        heapi(a, n, i, key_custom, cmp_custom)
    
    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapi(a, i, 0, key_custom, cmp_custom)
    
    return a

# print(heap_sort(list(map(int, input().split())), cmp_custom = lambda a, b: b - a))