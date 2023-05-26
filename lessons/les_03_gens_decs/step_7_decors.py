'''
Если нужно будет написать ещё какой-то сбор информации о работе функции
- Замерять память (мемори профайлер)
- ...

Т.е. нужно не меняя функционал функции добавить к ней дополнительное поведение
'''


def log_time(func):
    def wrapper(*args, **kwargs):


        result = func(*args, **kwargs)


        return result
    return wrapper


@log_time
def make_hello(name):
    result = f'{name}, hello!'
    return result


def sum_it(*args):
    print(f'sum {len(args)} nums')
    result = sum(*args)
    return result


# Пример работы декоратора
wrapper = log_time(make_hello)
result = wrapper('Vlad')
print(result)

print(make_hello('Vlad'))