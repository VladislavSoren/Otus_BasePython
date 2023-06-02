"""
batteries included (батарейки в комплекте)

wraps используется для сохранения совпадения сигнатуры функций
после применения пользовательских декораторов
"""

from functools import wraps


def show_args(func):

    @wraps(func)
    def wrapper(*args):
        args_str = ", ".join(map(str, args))
        print("proc_func",
              func.__name__,
              "with args:", args_str)
        result = func(*args)
        return result
    return wrapper


@show_args
def sum_nums(*args):
    return sum(args)


def maim():
    print(sum_nums)
    print(sum_nums.__name__)
    # print(sum_nums.__wrapped__) -> можно получить доступ к оригинальной вложенной функци и
    res = sum_nums(1, 2, 3)
    print(res)


if __name__ == '__main__':
    maim()


