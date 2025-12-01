def factorial_recursive(n: int) -> int:
    '''
    Считывает целое число n

    Вычисляет факториал числа от n до 1 рекурсивно

    Возвращает факториал числа
    '''
    if n < 0:
        raise ValueError("Факториал отрицательного числа не существет")
    if n == 1 or n == 0:
        return 1
    
    return n * factorial_recursive(n - 1)

# print(factorial_recursive(int(input())))