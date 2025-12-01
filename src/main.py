from src.fact_fibo.factorial import factorial
from src.fact_fibo.factorial_recursive import factorial_recursive
from src.fact_fibo.fibo import fibo
from src.fact_fibo.fibo_recursive import fibo_recursive

from src.sort_methods.bubble_sort import bubble_sort
from src.sort_methods.counting_sort import counting_sort
from src.sort_methods.heap_sort import heap_sort
from src.sort_methods.quick_sort import quick_sort
from src.sort_methods.radix_sort import radix_sort
from src.sort_methods.bucket_sort import bucket_sort

from src.Stack import Stack

from src.test_generators.rand_int_array import rand_int_array
from src.test_generators.nearly_sorted import nearly_sorted
from src.test_generators.reverse_sorted import reverse_sorted
from src.test_generators.many_duplicates import many_duplicates
from src.test_generators.rand_float_array import rand_float_array

from src.benchmark_sorts import benchmark_sorts
from src.timeit_once import timeit_once

def main() -> None:
    '''
    Основная функция мини-пакета

    Позволяет запускать все возможные доступные функции с соответствующими аргументами через консоль
    Выводит результат выполнения функции в консоль
    '''

    pretty: bool = False # красивость интерфейса (инатор обрёл сознание и выгорание); если не удобно, то можно заменить на False
    
    end_print = '''
    ⠀⠀⠀⠀⠀⠀⠀⠀ ⠈⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⡇⠀⢶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⢋⡼⠁⠀⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣿⣳⠏⠀⣠⠞⣡⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⡄⢸⣯⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠳⠸⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⡀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣁⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⢸⡟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⢻⢿⣷⢀⣀⣀⣀⡀⠀
    ⢸⡇⠀⣶⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠶⣒⣒⣿⣋⣥⣄⡉⢻⣆
    ⢸⣿⠈⣇⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⠶⢶⣿⠁⠀⢸⡇⢰⣿
    ⠀⢻⣆⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠒⣾⣯⣤⣴⠟⣡⣿⠃
    ⠀⠈⢿⣎⠻⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣿⣿⣭⣥⣴⡿⠟⠁⠀
    ⠀⠀⠈⢿⣷⣄⠑⣦⡄⠀⠀⠀⣀⠀⢛⣻⣿⡟⠉⠉⠉⠀⠀⠀⠀⠀
    ⠀⣴⡶⠶⠿⠿⢿⣶⣤⣤⣤⣤⣽⣿⠿⠛⣛⣟⣷⡆⠀⠀⠀⠀⠀⠀
    ⠀⠛⠷⠶⣤⣤⣤⣤⣴⣾⣿⣿⣶⣦⣤⣶⣶⡾⠟⠁⠀⠀⠀⠀⠀⠀
                    '''
    
    if pretty:
        start_print = "\nEnter command =_="
    else:
        start_print = "\nEnter command:"

    #здесь все функции разделённые на типы
    functions_n = {
        'fact': factorial,
        'fact_rec': factorial_recursive,
        'fibo': fibo,
        'fibo_rec': fibo_recursive
    }

    functions_sort = {
        "counting_sort": counting_sort,
        "radix_sort": radix_sort
    }

    functions_sort_compare_key = {
        "bubble_sort": bubble_sort,
        "heap_sort": heap_sort,
        "quick_sort": quick_sort
    }

    #словарь для кастомных стэков
    stacks = {}

    #рандомные массивы для бэнчмарков
    test_arrays = {
        "small_sorted": [1, 2, 3, 4, 5],
        "small_random": [3, 1, 4, 2, 5],
        "small_reversed": [5, 4, 3, 2, 1],
        "medium_random": rand_int_array(100, 0, 1000),
        "large_random": rand_int_array(1000, 0, 10000),
        "many_duplicates": many_duplicates(50, k_unique=5),
        "nearly_sorted_10": nearly_sorted(100, swaps=10),
        "nearly_sorted_50": nearly_sorted(100, swaps=50),
        "reverse_sorted_100": reverse_sorted(100),
        "all_duplicates": [5] * 100,
    }

    test_arrays_float = {
        "float_small": rand_float_array(10, 0.0, 1.0),
        "float_medium": rand_float_array(100, 0.0, 1.0),
        "float_large": rand_float_array(1000, 0.0, 1.0),
        "float_sorted": [i/100 for i in range(100)],
        "float_reversed": [i/100 for i in range(99, -1, -1)],
    }

    print("=============WORK STARTED=============")

    while True:

        print(start_print)
        data = input().strip()

        try:
            function, args = data.split(" ", maxsplit=1)
        except ValueError:
            function = data
            args = None

        # print("Function:", function)

        try:

            if function in functions_n.keys():
                try:
                    arg = int(args)
                except ValueError:
                    raise ValueError("need int value for func")
                
                func = functions_n[function]
                res, timing = timeit_once(func, arg)

                print(f"Результат функции: {res}")
                print(f"Время работы: {timing} мкс")

            elif function in functions_sort.keys():
                try:
                    arr = list(map(int, args.split()))
                except (ValueError, AttributeError):
                    print("Неверный ввод списка чисел")
                    continue

                func = functions_sort[function]
                sorted_arr, timing = timeit_once(func, arr)

                print(f"Отсортированный массив: {sorted_arr}")
                print(f"Время работы: {timing} мкс")

            elif function in functions_sort_compare_key.keys():
                try:
                    func_args = args.split("; ")
                    # print("func_args", func_args)
                    cmp = None
                    key = None
                    arr = list(map(int, func_args[0].split()))
                    try:
                        arg1 = func_args[1]
                        if "cmp" in arg1:
                            cmp = eval(arg1.split("=")[1])
                        elif "key" in arg1:
                            key = eval(arg1.split("=")[1])
                        else:
                            raise ValueError
                        
                        arg2 = func_args[2]
                        if "cmp" in arg2:
                            cmp = eval(arg2.split("=")[1])
                        elif "key" in arg2:
                            key = eval(arg2.split("=")[1])
                        else:
                            raise ValueError
                    except IndexError:
                        pass

                except (ValueError, AttributeError):
                    print("Ошибка: необходимо передать список чисел через пробел")
                    continue


                # print(arr, key, cmp)

                func = functions_sort_compare_key[function]
                sorted_arr, timing = timeit_once(func, arr, key, cmp)

                print(f"Отсортированный массив: {sorted_arr}")
                print(f"Время работы: {timing} мкс")

            elif function == "bucket_sort":
                args = args.split("; ")
                arr = list(map(float, args[0].split()))
                buckets = None
                if len(args) == 2:
                    buckets = int(args[1])

                func = bucket_sort
                sorted_arr, timing = timeit_once(func, arr, buckets)

                print(f"Отсортированный массив: {sorted_arr}")
                print(f"Время работы: {timing} мкс")



            elif function == "benchmark":
                res_sort = benchmark_sorts(test_arrays, functions_sort)
                res_sort_key_cmp = benchmark_sorts(test_arrays, functions_sort_compare_key)
                res_sort_float = benchmark_sorts(test_arrays_float, {"bucket_sort": bucket_sort})
                results = res_sort | res_sort_key_cmp | res_sort_float
                
                print("\nРезультаты бенчмарка сортировок:")
                for algo_name, array_times in results.items():
                    print(f"\n{algo_name}:")
                    for array_name, time_taken in array_times.items():
                        print(f"  {array_name}: {time_taken} мкс")

            elif function == "show_arrays":
                print("Текущие тестовые массивы:")
                for name, arr in test_arrays.items():
                    if len(arr) > 10:
                        print(f"  {name}: {arr[:10]}... (длина={len(arr)})")
                    else:
                        print(f"  {name}: {arr} (длина={len(arr)})")
                
                print("\nВещественные тестовые массивы:")
                for name, arr in test_arrays_float.items():
                    if len(arr) > 10:
                        print(f"  {name}: {[f'{x:.3f}' for x in arr[:10]]}... (длина={len(arr)})")
                    else:
                        print(f"  {name}: {[f'{x:.3f}' for x in arr]} (длина={len(arr)})")

            elif function == "Stack":
                args = args.split("; ")
                name = args[0]
                arr = []
                if len(args) > 1:
                    arr = list(map(int, args[1].split()))

                stacks[name] = Stack(arr)

                print(f"Создан стэк {name}: {stacks[name].arr}")

            elif function in stacks.keys():
                args = args.split("; ")
                stack_func = args[0]
                # print(stack_func)

                if stack_func == "push":
                    num = int(args[1])
                    stacks[function].push(num)
                    print(f"Стэк {function}: {stacks[function].arr}")

                elif stack_func == "is_empty":
                    res = stacks[function].is_empty()
                    if res:
                        print(f"Стэк {function} пустой")
                    else:
                        print(f"Стэк {function} не пустой: {stacks[function].arr}")

                elif stack_func == "peek":
                    res = stacks[function].peek()
                    print(f"Верхний элемент стэка {function}: {res}")

                elif stack_func == "pop":
                    res = stacks[function].pop()
                    print(f"Забранный верхний элемент стэка {function}: {res}")
                    print(f"Стэк {function}: {stacks[function].arr}")

                elif stack_func == "min":
                    res = min(stacks[function])
                    print(f"Минимальный элемент списка {function}: {res}")

                elif stack_func == "len":
                    res = len(stacks[function])
                    print(f"Длина стэка {function}: {res}")

                else:
                    raise ValueError("Stack function not found")

                


            elif function == "help":
                print("Доступные функции:")
                print("     Числовые:", ", ".join(functions_n.keys()))
                print(f"     Сортировки: {", ".join(functions_sort.keys())}, bucket_sort (для float от 0 до 1)")
                print("     Стэки:")
                print("           Инициализация: Stack <name>; <array>")
                print("           Функции: push, is_empty, peek, pop, min, len")
                print("     benchmark - запуск бенчмарка всех сортировок")
                print("     show_arrays - показ созданных рандомных массивов для бенчмарков")
                print("     q - выход\n")

            elif function == "q":
                print("=============WORK COMPLETE=============")
                if pretty:
                    print(end_print)
                return 0
            
            else:
                raise IndexError("Function not found")  
            
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()