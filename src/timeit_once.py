import time

def timeit_once(func, *args, **kwargs):
    '''
    Получает функцию и её аргументы

    Проводит единичный бэнчмар функции для данных аргументов

    Возвращает результат функции и время её выполнения в микросекундах
    '''
    start_time = time.perf_counter()
    res = func(*args, **kwargs)
    end_time = time.perf_counter()
    timing = end_time - start_time
    micro = timing * 1_000_000
    micro = int(micro * 10000) / 10000
    return res, micro
