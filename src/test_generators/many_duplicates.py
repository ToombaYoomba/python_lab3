import random

def many_duplicates(n: int, k_unique=5, *, seed_custom=None) -> list[int]:
    random.seed(seed_custom)

    unique = random.sample(range(0, 1001), k_unique)
    not_unique_numbers = [random.choice([i for i in range(0, 1001) if i not in unique])] * (n - k_unique)

    random_arr = unique + not_unique_numbers
    random.shuffle(random_arr)

    return random_arr


