"""

__main__.py можно стартануть при вызове директории проекта, т.е. "python otus-1"

Теперь другим разрабам не нужно задумываться какой файлик у меня стартовый, т.к.
при вызове директории автоматом запустится __main__.py

Через * всё импортируется в глобальное пространство имён, и если кто-то переопределил (намеренно или случайно)
какие-то вещи, например max, min = min, max, да и ещё не правильно - жди беды
"Кто подставил кролика Роджера"? - ахахахах

*** Не закакивай пространство имён бро :)

По PEP:
- Один импорт - в одной строке!
"""

import functools
import itertools
# import utils
# import math, functools, itertools
import math
import sys

from requests import get

from helpers import get_currency_rate
from utils import (get_currency_rate,
                   BASE_CURRENCY,
                   )
# from otus-2 imort

# from utils import *

# print(dir(utils))

print(*sys.path, sep='\n')

def main():
    print('started __main__.py')
    # currency_rate = get_currency_rate()
    # print(currency_rate)
    # print(BASE_CURRENCY)
    # print(f'Минимально значение в списке {[1, 20]}: {min([1, 20])}')
    # print(math.sin(math.pi / 2), functools.partial, itertools.cycle)
    # print(get)



if __name__ == '__main__':
    main()
