from pathlib import Path
import sys

BD_PATH = Path(__file__).parent / 'db'
print('Путь к директории с БД:', BD_PATH)
sys.path.append(str(BD_PATH))
print(*sys.path, sep='\n')

from parsers.parser_1 import get_site_info

get_site_info()