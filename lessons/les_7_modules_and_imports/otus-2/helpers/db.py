"""

utils вне зоны нашей видимости (его нет в path)

__name__ == '__main__' - знакомая правктика

"""

from pathlib import Path

ROOT = Path(__file__).parent
ROOT = ROOT.parent
print('Путь к исполняемому файлу:', __file__)
print('Директория на уровень выше:', ROOT)
# print('Директория на 2 уровеня выше:', ROOT.parent)

import sys

sys.path.append(str(ROOT))
print(*sys.path, sep='\n')

from decimal import Decimal
from utils import save_currency_rate


def update_db():
    save_currency_rate('USD', 15)


if __name__ == '__main__':
    update_db()