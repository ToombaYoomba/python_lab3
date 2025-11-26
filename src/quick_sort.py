from random import choice

def quick_sort(a: list[int]) -> list[int]:
    if len(a) <= 1:
        return a
     
    else:
        pick: int = choice(a)
        left: list[int] = []
        middle: list[int] = []
        right: list[int] = []
        for e in a:
            if e < pick:
                left.append(e)
            elif e == pick:
                middle.append(e)
            else:
                right.append(e)
        
        return quick_sort(left) + middle + quick_sort(right)
    
# print(quick_sort(list(map(int, input().split()))))