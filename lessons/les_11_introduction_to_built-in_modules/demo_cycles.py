from  itertools import cycle, repeat
from pprint import pprint


def demo_cycle():
    names = cycle([
        'Tim,',
        'Bob',
        'Sam',
    ])
    for _ in range(10):
        print(next(names))

    ideas = [
        'Job 1',
        'Job 2',
        'Job 3',
        'Job 4',
        'Job 5',
    ]

    for idea, name in zip(ideas, names):
        print(idea, 'for', name)


def demo_repeat():
    num_2 = repeat(2, times=3)  # итерируемый объект, по умолчанию times - бесконечно

    pprint(list(map(pow, range(1, 10), num_2)))


def maim():
    # demo_cycle()
    demo_repeat()


if __name__ == '__main__':
    maim()
