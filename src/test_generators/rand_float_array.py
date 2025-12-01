import random

def rand_float_array(n: int, lo=0.0, hi=1.0, *, seed_custom=None) -> list[float]:
    '''
    Принимает длину массива, минимальный и максимальный порог для чисел и кастомный сид

    Генерирует рандомный массив дробных чисел от lo до hi

    Возвращает массив дробных чисел
    '''
    random.seed(seed_custom)

    arr = [random.uniform(lo, hi) for i in range(n)]

    return arr