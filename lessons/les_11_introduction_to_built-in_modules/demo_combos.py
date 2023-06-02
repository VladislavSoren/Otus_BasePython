"""
уникальные сочетания

полезная библа по комбинациям "more-itertools"

"""
# more-itertools (grouper, batched...)
from pprint import pprint
from itertools import (combinations,  # комбинации
                       permutations,  # перестановки
                       combinations_with_replacement,  # комбинации с заменой (повторением)
                       product)  # сочетания между двумя итерируемыми объёктами


names_male = [
    'Tim',
    'Bob',
    'Sam',
]

names_female = [
    'Kate',
    'Mary',
]

names = names_male + names_female


def demo_combinations():
    pairs = combinations(names, 2)
    pprint(list(pairs))


def demo_permutations():
    pairs = permutations(names, 2)
    pprint(list(pairs))


def demo_combinations_with_replacement():
    pairs = combinations_with_replacement(names, 2)
    pprint(list(pairs))


def demo_product():
    pairs = product(names_male, names_female)
    pprint(list(pairs))



def maim():
    # demo_combinations()
    # demo_permutations()
    # demo_combinations_with_replacement()
    demo_product()

if __name__ == '__main__':
    maim()

