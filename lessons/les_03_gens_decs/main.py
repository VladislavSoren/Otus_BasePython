import time

#####################################################
# Задачи те же что и в прошлом модуле, баг или фича?
#####################################################

'''
9.
Создайте функцию, которая принимает неограниченное число аргументов (чисел),
и возвращает только простые числа в виде списка (list)
'''


# Функция проверки числа на простоту
def num_is_simple(a: int) -> bool:
    k = 0
    for divisor in range(2, a // 2+1):
        if a % divisor == 0:
            k = k+1
    if k <= 0:
        return True
    else:
        return False


# Функция получения списка простых чисел
def get_simple_numbers_list(*args):

    simple_numbers_list = [number for number in args if num_is_simple(number) is True]
    return simple_numbers_list


args = [num for num in range(100)]

simple_numbers_list = get_simple_numbers_list(*args)
print(simple_numbers_list)


'''
10.
Создайте функцию, которая принимает в себя строчку и возвращает список (list) 
с уникальными символами из этой строчки. 
Например, при вызове функцию с передачей аргументом строкой 'aabcdd' 
должно быть возвращено ['a', 'b', 'c', 'd'] (порядок элементов не важен)
'''


def get_unique_symbols_list(inner_str: str) -> list:

    symbols_list = [sym for sym in inner_str]
    symbols_set = set(symbols_list)
    unique_symbols_lis = list(symbols_set)
    return unique_symbols_lis


inner_str = '12781524651-1=-2238197362173gbgbvdcdscsw123'
unique_symbols_lis = get_unique_symbols_list(inner_str)
print(unique_symbols_lis)


# Декоратор оценки времени работы функции
def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter_ns()
        res = function(*args)
        print('Exec time: ', time.perf_counter_ns() - start_time) # можно логгировать
        return res
    return wrapped

@time_of_function
def func(first, second):
    return bin(int(first, 2) + int(second, 2))

print(func)

print(func("111", "0000"))