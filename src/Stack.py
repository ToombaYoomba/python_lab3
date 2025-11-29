class Stack:
    def __init__(self):
        self.arr: list[int] = list()
        self.mini: int | None = None

    def __len__(self) -> int:
        return len(self.arr)
    
    def new_mini(self) -> None:
        if not self.arr:
            self.mini = None
        else:
            self.mini = min(self.arr)

    def push(self, x: int) -> None:
        self.arr.append(x)

        self.new_mini()

    def is_empty(self) -> bool:
        return not self.arr
    
    def peek(self) -> int:
        if not self.arr:
            raise IndexError("peek from empty stack")
        return self.arr[-1]
    
    def pop(self) -> int:
        if not self.arr:
            raise IndexError("pop from empty stack")
        
        popped = self.arr.pop()

        self.new_mini()
        
        return popped
    
    def min(self) -> int:
        if self.mini is None:
            raise IndexError("no min in empty stack")
        return self.mini