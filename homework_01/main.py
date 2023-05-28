"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers) -> list:
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """

    return [number ** 2 for number in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


# Функция проверки числа на простоту
def is_prime(a: int) -> bool:
    k = 0

    if a in [0, 1]:
        result = False
    else:
        for divisor in range(2, a // 2+1):
            if a % divisor == 0:
                k = k+1
        if k <= 0:
            result = True
        else:
            result = False
    return result


def filter_numbers(int_numbers_list, filter_type) -> list:
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

    if filter_type == ODD:
        result = list(filter(lambda x: x % 2 != 0, int_numbers_list))
    elif filter_type == EVEN:
        result = list(filter(lambda x: x % 2 == 0, int_numbers_list))
    elif filter_type == PRIME:
        result = list(filter(is_prime, int_numbers_list))
    else:
        result = ['Unknown filter_type']

    return result
