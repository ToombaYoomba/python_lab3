def heapi(a: list[int], n: int, i: int) -> None:
    largest: int = i
    left: int = 2 * i + 1
    right: int = 2 * i + 2

    if left < n and a[left] > a[largest]:
        largest = left

    if right < n and a[right] > a[largest]:
        largest = right

    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapi(a, n, largest)

def heap_sort(a: list[int]) -> list[int]:
    a: list[int] = a.copy()
    n: int = len(a)
    
    for i in range(n // 2 - 1, -1, -1):
        heapi(a, n, i)
    
    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapi(a, i, 0)
    
    return a

# print(heap_sort(list(map(int, input().split()))))