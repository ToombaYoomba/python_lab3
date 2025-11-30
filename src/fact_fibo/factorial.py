def factorial(n: int) -> int:
    fac: int = 1

    if n < 0:
        raise ValueError("Факториал отрицательного числа не существет")
    if n == 0 or n == 1:
        return 1
    
    for i in range(1, n + 1):
        fac = fac * i

    return fac

# print(factorial(int(input())))