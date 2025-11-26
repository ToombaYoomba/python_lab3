def bubble_sort(a: list[int]) -> list[int]:
    N: int = len(a)

    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

    return a

# print(bubble_sort(list(map(int, input().split()))))