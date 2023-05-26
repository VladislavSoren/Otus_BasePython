import time
from functools import wraps

'''
Кэширующие декораторы
'''


def log_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.monotonic_ns()
        result = func(*args, **kwargs)
        end = time.monotonic_ns()
        print(f'Exec time {func.__name__} {end - start}')
        return result
    return wrapper


@log_time
def make_hello(name):
    '''
    :param name:
    :return:
    '''
    time.sleep(1)
    result = f'{name}, hello!'
    return result


@log_time
def sum_it(*args):
    print(f'sum {len(args)} nums')
    result = sum(args)
    return result


# print(make_hello('Vlad'))
# print(f'Sum res: {sum_it(*[el for el in range(100)])}')
print(make_hello.__name__)
print(make_hello.__doc__)