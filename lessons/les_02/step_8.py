# def sum_it(a, b, c=0):
#     return a + b + c


def sum_it(*args):

    result = 0
    for el in args:
        result += el
    return result


args = [1, 2, 3, 4, 5, 10]

result = sum_it(*args)
pass