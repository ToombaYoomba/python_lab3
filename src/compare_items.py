from typing import TypeVar, Callable, Any

def compare_items(x: TypeVar, y: TypeVar, key: Callable[[TypeVar], Any] | None = None,
                 cmp: Callable[[TypeVar, TypeVar], int] | None = None) -> int:
    
    if key is None:
        x_val = x
    else:
        x_val = key(x)

    if key is None:
        y_val = y
    else:
        y_val = key(y)
    
    if cmp is not None:
        if cmp(x, y) < 0:
            return -1
        elif cmp(x, y) > 0:
            return 1
        else:
            return 0
    
    if key is None:
        x_val = x
    else:
        x_val = key(x)

    if key is None:
        y_val = y
    else:
        y_val = key(y)
    
    if x_val < y_val:
        return -1
    elif x_val > y_val:
        return 1
    else:
        return 0