"""

Циклический импорт - зло

"""

import sys


from helpers import get_currency_rate  # inner_logic
from utils import (get_currency_rate,
                   BASE_CURRENCY,
                   )


# print(*sys.path, sep='\n')


def main():
    print('started __main__.py')
    currency_rate = get_currency_rate()
    print(currency_rate)
    print(BASE_CURRENCY)


if __name__ == '__main__':
    main()
