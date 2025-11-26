def fibo_recursive(n: int) -> int:
    if n < 1:
        raise ValueError("Члены последовательности Фибоначчи начинаются с 1")
    if n == 1 or n == 2:
        return 1
    
    return fibo_recursive(n - 2) + fibo_recursive(n - 1) 

# print(fibo_recursive(int(input())))