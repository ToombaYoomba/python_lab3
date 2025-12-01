def radix_sort(a: list[int], base: int = 10) -> list[int]:
    '''
    Получает массив целых чисел

    Сортирует массив, последовательно сортируя числа по их разрядам
    Каждый раз сортирует по разряду. Проходится столько раз, сколько разрядов в самом большом числе массива
    
    Возвращает отсортированный массив
    '''
    if not a:
        return []
    
    leni = len(str(max(a)))

    for i in range(leni):
        rads = [[] for _ in range(base)]

        for elem in a:
            digit = (elem // base ** i) % base
            rads[digit].append(elem)

        a = [x for queue in rads for x in queue]
        # print(a)

    return a

# print(radix_sort(list(map(int, input().split()))))