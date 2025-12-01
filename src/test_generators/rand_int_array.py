import random

def rand_int_array(n: int, lo: int, hi: int, *, distinct=False, seed_custom=None) -> list[int]:
    '''
    Принимает длину массива, минимальный и максимальный порог для чисел, все ли числа уникальны и кастомный сид

    Генерирует рандомный массив целых чисел от lo до hi
    Если distinct==True, то в массиве все числа уникальны

    Возвращает массив целых чисел
    '''
    random.seed(seed_custom)

    if distinct:
        arr = random.sample(range(lo, hi), n)
    else:
        arr = [random.randint(lo, hi) for i in range(n)]

    return arr