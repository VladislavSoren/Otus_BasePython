import sys

'''
generator expression
* генератор хранит своё состояние

IOPS operations
'''

max_nums = 10  # memory O(1)

# generator expression <genexpr>
nums = (el for el in range(max_nums))  # memory O(1)
print('Занимаемый размер памяти генератора в байтах: ', sys.getsizeof(nums))

# nums_sum = sum(nums) # одноразовый, коль выполнил - создай новый
# print(nums_sum)

print(next(nums))
print(next(nums))
print(next(nums))

nums = (el for el in range(max_nums))  # memory O(1)
nums_sum = sum(nums)
print(next(nums))

"""
iterator VS generator

* generator умеет чуть больше, чем просто итерироваться
* корутина по своей сути и есть генератор
"""
nums.send()
nums.close()
nums.throw()

