import time

def timeit_once(func, *args, **kwargs):
    start_time = time.perf_counter()
    res = func(*args, **kwargs)
    end_time = time.perf_counter()
    timing = end_time - start_time
    return res, timing
