def factorial_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("Факториал отрицательного числа не существет")
    if n == 1 or n == 0:
        return 1
    
    return n * factorial_recursive(n - 1)

# print(factorial_recursive(int(input())))