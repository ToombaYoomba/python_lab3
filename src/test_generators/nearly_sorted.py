import random


def nearly_sorted(n: int, swaps: int, *, seed_custom=None) -> list[int]:
    random.seed(seed_custom)

    arr = sorted(random.sample(range(0, 1001), n))
    # print(arr)

    for _ in range(swaps):
        fi, se = random.randint(0, n-1), random.randint(0, n-1)
        # print(fi, se)
        arr[fi], arr[se] = arr[se], arr[fi]

    return arr


# print(nearly_sorted(10, swaps=3))
