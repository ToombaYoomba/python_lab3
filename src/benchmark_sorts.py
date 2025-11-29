from typing import Callable
from src.timeit_once import timeit_once

def benchmark_sorts(arrays: dict[str, list], algos: dict[str, Callable]) -> dict[str, dict[str, float]]:
    results: dict[str, dict[str, float]] = {}
    
    for algo_name, sort_func in algos.items():
        results[algo_name] = {}
        
        for array_name, array in arrays.items():

            sorted_array, timing = timeit_once(sort_func, array)
            results[algo_name][array_name] = timing
    
    return results