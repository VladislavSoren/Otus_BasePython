import time
from functools import reduce

'''

lambda + map работает быстрее колхозного цикла со списком

Все эти функции применяются в  функциональном подходе (программирования), т.е.
мы не изменяем данные, не делаем мутации, а создаём новые объекты!

Экономия памяти, т.к. работаем с генераторами

'''


######################
# Измерение скоростей
######################
nums = [num for num in range(10000)]

t1 = time.perf_counter_ns()
nums_sqrs_list = []
for num in nums:
    sq = num ** 2
    nums_sqrs_list.append(sq)
print(time.perf_counter_ns() - t1)
print(nums_sqrs_list)


t1 = time.perf_counter_ns()
res = list(map(lambda a: a**2, nums))
print(time.perf_counter_ns() - t1)
print(res)

################################################
# Несколько списков (zip в рамках lambda + map)
################################################
nums = [1,2,3,5]
powers = [2,3,4,3]
print(list(map(lambda x, y: x**y, nums, powers)))


################################################
# filter
################################################
events = list(filter(lambda x: x % 2 == 0, range(10)))
print(events)


################################################################################
# reduce (скользящее окно по результату функции и следующему итерируему объекту)
# Аккумуляция значений!
################################################################################
def add(a, b):
    res = a + b
    print('a + b =', res)
    return res

print(reduce(add, nums, 100))


def combine_sets(set1, set2):
    return set1 | set2

print(
    reduce(
        combine_sets, [
            {1, 2},
            {5, 6},
            {1, 3},
            {5, 6, 7}
        ]
    )
)







