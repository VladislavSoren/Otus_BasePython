"""
Заранее предусмотрите, чтобы fillvalue соответствовало
наименьшей коллекции (уникальные сочитания)

"""

from itertools import zip_longest


def maim():
    names = [
        'Tim',
        'Bob',
        'Sam',
        'Jim'
    ]
    acts = [
        'wash',
        'clean',
    ]

    for name, act in zip_longest(names, acts, fillvalue="rest"):
        print(name, 'must', act)


if __name__ == '__main__':
    maim()
