import random

def reverse_sorted(n: int) -> list[int]:
    '''
    Принимает длину массива

    Генерирует рандомный, отсортированный в обратном порядке массив целых чисел

    Возвращает массив целых чисел
    '''
    arr = sorted(random.sample(range(0, 1001), n), reverse=True)

    return arr