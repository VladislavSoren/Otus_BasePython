# Путевой кастыль
from pathlib import Path
import sys

BD_PATH = Path(__file__).parent.parent.parent
sys.path.append(str(BD_PATH))
print(*sys.path, sep='\n')

from .views import router