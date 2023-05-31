"""
setUp выполняется перед каждым тестом

Тесты должны быть атомарными, т.е. чтобы их нельзя было разделить

Пишем тесты на пайтест, но в любом случае фишки из юнит тест тоже можно тянуть

Параметризация нужна для того, чтобы проверить несколько кейсов по одинаковому правилу

Параметризация фикстур

indirect=["solver_mix"] -> косвенно пробрасываем solver_mix,
иначе будет восприниматься кортеж solver_mix, expected

* Вложенные фикстуры и мокирование
"""

from pathlib import Path
import sys

# LOC_ROOT_PATH = Path(__file__).parent / 'db'
LOC_ROOT_PATH = Path(__file__).parent.parent
print('Путь к директории с БД:', LOC_ROOT_PATH)
sys.path.append(str(LOC_ROOT_PATH))
# print(*sys.path, sep='\n')


from unittest import TestCase
from pytest import fixture, mark, param

from solver import Solver


class SolverTestCase(TestCase):

    def setUp(self) -> None:
        self.solver = Solver(2, 3)

    def test_add(self):
        result = self.solver.add()
        self.assertEqual(result, 5)

    def test_mul(self):
        result = self.solver.mul()
        self.assertEqual(result, 6)


@fixture()
def solver():
    return Solver(2, 3)


## Используется но не часто
# @fixture(
#     params=[
#         (1, 2),
#         (3, 4)
#     ]
# )
# def solver_mix(request):
#     a, b = request.param
#     return Solver(a, b)

@fixture()
def solver_mix(request):
    a, b = request.param
    return Solver(a, b)


class TestSolver:

    def test_add(self, solver: Solver):
        res = solver.add()
        assert res == 5

    def test_add_zero(self, solver: Solver):
        solver.a = 0
        assert solver.add() == 3

    def test_mul(self, solver: Solver):
        res = solver.mul()
        assert res == 6

    @mark.parametrize("a, b, expected",
                      [
                          (1, 2, 3),
                          param(0, 0, 0, id='all_zeros'),
                          (0, 1, 1)
                      ])
    def test_add_many(self, a, b, expected):
        solver = Solver(a, b)
        result = solver.add()
        assert result == expected

    @mark.parametrize(
        'solver_mix, expected',
        [
            param([2, 4], 8),
            param([2, 3], 6),
            param([2, 5], 10, id='ten-expected '),
        ],
        indirect=["solver_mix"],
    )
    def test_mul_many(self, solver_mix: Solver, expected):
        result = solver_mix.mul()
        assert result == expected



