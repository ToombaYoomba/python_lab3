from collections import defaultdict

def counting_sort(a: list[int]) -> list[int]:
    if not a:
        return []
    
    counti = defaultdict(int)

    for i in a:
        counti[i] += 1

    mi = min(a)
    ma = max(a)

    ans: list[int] = []

    for i in range(mi, ma+1):
        ans += [i] * counti[i]

    return ans

# print(counting_sort(list(map(int, input().split()))))