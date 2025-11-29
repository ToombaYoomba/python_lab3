def fibo(n: int) -> int:
    fib1: int = 1
    fib2: int = 1

    if n < 1:
        raise ValueError("Члены последовательности Фибоначчи начинаются с 1")
    if n == 1 or n == 2:
        return 1
    
    fib: int
    
    for i in range(n - 2):
        fib = fib1 + fib2
        fib1, fib2 = fib2, fib


    return fib

# print(fibo(int(input())))