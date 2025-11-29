import random

def rand_int_array(n: int, lo: int, hi: int, *, distinct=False, seed_custom=None) -> list[int]:
    random.seed(seed_custom)

    if distinct:
        arr = random.sample(range(lo, hi), n)
    else:
        arr = [random.randint(lo, hi) for i in range(n)]

    return arr