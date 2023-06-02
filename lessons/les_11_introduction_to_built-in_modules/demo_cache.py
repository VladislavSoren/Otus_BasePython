"""
Просьба написать рекурсивную функцию на собесе...
* Какие примеры использование рекурсии в реальных проектах?

Применение кэширования для аргумента n

Пример использования кэша:
Мы в течении 5 минут отдаём одинаковые прогнозы пользователям по кэшу первого запроса, т.к.
всё равно за 5 минут ничего кардинально не изменится, а нагрузка на наше приложение ниже
"""

from functools import cache, lru_cache


@cache
def factorial(n):
    print("get factorial for n", n)
    # Базовый случай
    if n < 2:
        return n
    return n * factorial(n - 1)


def maim():
    print(factorial(3))
    # print(factorial(4))
    # print(factorial(5))
    print(factorial(6))


if __name__ == '__main__':
    maim()
