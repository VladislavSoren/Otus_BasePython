import sys

'''
А надо ли иметь все числа в памяти ОДНОВРЕМЕННО???



'''

max_nums = 10  # memory O(1)

# simple list
nums = [el for el in range(max_nums)]  # memory O(n)
print('Занимаемый размер памяти списка в байтах: ', sys.getsizeof(nums))

nums_sum = sum(nums)
print(nums_sum)

print(nums[0])
print(nums[1])
print(nums[2])

