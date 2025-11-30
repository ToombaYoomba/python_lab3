def bucket_sort(a: list[float], buckets_n: int | None = None) -> list[float]:
    if buckets_n is None:
        buckets_n = len(a)
    
    buckets = [[] for i in range(buckets_n)]
    # print(buckets)

    for elem in a:
        bucket_number = int(buckets_n * elem)
        buckets[bucket_number].append(elem)

    for i in range(len(buckets)):
        buckets[i] = sorted(buckets[i])

    res = []

    for bucket in buckets:
        res += bucket

    return res

# print(bucket_sort(list(map(float, input().split()))))