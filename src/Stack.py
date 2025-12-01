class Stack:
    '''
    Класс стэка на списке

    Принимает начальный массив стэка

    В себе хранит массив стэка
    '''
    def __init__(self, arr: list[int] = []):
        self.arr: list[int] = arr

    def __len__(self) -> int:
        '''
        Возвращает длину стэка
        '''
        return len(self.arr)
    
    def __getitem__(self, index):
        '''
        Нужен для того, чтобы при вызове min() итератор мог получить элементы массива внутри класса
        '''
        return self.arr[index]

    def push(self, x: int) -> None:
        '''
        Добавляет число вверх стэка
        '''
        self.arr.append(x)

    def is_empty(self) -> bool:
        '''
        Проверяет, если стэк пустой
        '''
        return not self.arr
    
    def peek(self) -> int:
        '''
        Возвращает верхний элемент стэка
        '''
        if not self.arr:
            raise IndexError("peek from empty stack")
        return self.arr[-1]
    
    def pop(self) -> int:
        '''
        Возвращает верхний элемент стэка и достаёт его из стэка
        '''
        if not self.arr:
            raise IndexError("pop from empty stack")
        
        popped = self.arr.pop()
        
        return popped
    
# a = Stack([0, 1, 2])
# print(min(a))
    
