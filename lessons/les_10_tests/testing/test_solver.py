from pathlib import Path
import sys

# LOC_ROOT_PATH = Path(__file__).parent / 'db'
LOC_ROOT_PATH = Path(__file__).parent.parent
print('Путь к директории с БД:', LOC_ROOT_PATH)
sys.path.append(str(LOC_ROOT_PATH))
print(*sys.path, sep='\n')


from unittest import TestCase

from solver import Solver


class SolverTestCase(TestCase):

    def test_add(self):
        solver = Solver(2, 3)
        result = solver.add()
        self.assertEqual(result, 5)