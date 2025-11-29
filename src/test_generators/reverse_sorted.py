import random

def reverse_sorted(n: int) -> list[int]:
    
    arr = sorted(random.sample(range(0, 1001), n), reverse=True)

    return arr