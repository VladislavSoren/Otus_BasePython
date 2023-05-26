
'''
Мы используем генераторы когда:
- Нужно сэкономить память
- НЕ нужен параллельный доступ
- Нужно один раз пробежаться
- Асинхронка на базе генераторов (это порог вхождения в норм компании)
'''


max_nums = 10

# Для простых случаев
# nums = (el for el in range(max_nums))


# Прототип корутины
def nums_gen(max_nums):
    for el in range(max_nums):
        print('start')
        yield el  # not return!!!
        print('done')


nums = nums_gen(max_nums)
print(nums)
print(next(nums))
print(next(nums))
print(next(nums))
