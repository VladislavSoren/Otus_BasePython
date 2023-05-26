import time
from functools import wraps

'''
Кэширующие декораторы
'''


def log_time(logger=print):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.monotonic_ns()
            result = func(*args, **kwargs)
            end = time.monotonic_ns()
            logger(f'Exec time {func.__name__} {end - start}')
            return result
        return wrapper
    return inner


def my_logger(*args):
    for el in args:
        print(el, '!!!')


@log_time(my_logger)
def make_hello(name):

    result = f'{name}, hello!'
    return result


print(make_hello('Vlad'))
print(make_hello.__name__)
