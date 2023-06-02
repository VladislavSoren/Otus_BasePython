"""
Очередь с двумя концами (обычная очередь), т.е.
first in first out (FIFO)

chain nозволяет сделать список списков плоским (объединить в один список)
"""

from collections import deque
from itertools import chain

names_male = [
    'Tim',
    'Bob',
    'Sam',
]
names_female = [
    'Kate',
    'Mary',
]
names_list = [names_male, names_female, ['Vlad']]

# Сделать список списков плоским (объединить в один список)
names = list(chain.from_iterable(names_list))

def demo_deque():
    queue = deque(names_male)

    print(queue)
    print(queue.popleft())
    print(queue)
    print(queue.popleft())
    queue.append('Wow')
    queue.append('Any')
    print(queue)


def maim():
    demo_deque()


if __name__ == '__main__':
    maim()