import sys
import  time

'''
# list
Operation | Average Case | Amortized Worst Case
x in s | O(n)


# set - хэш таблица
x in s | O(1) | O(n)

Элементами могут быть ТОЛЬКО хешируемые объекты
 
Примечание:
Большинство неизменяемых встроенных объектов Python являются хешируемыми и имеют хеш-значение. 
Изменяемые контейнеры, такие как списки или словари, не имеют хеш-значений

'''

# def_list = [i for i in range(199999991)]
# # a = {15, 85.2, 'hello', 'hello'}
# a = set(def_list)
# t1 = time.time()
# print(type(a), 66666666 in a)
# print(time.time() - t1)
# '''
# <class 'set'> True
# 0.007999658584594727
# '''
#
# # b = [15, 85.2, 'hello', 'hello']
# b = def_list
# t1 = time.time()
# print(type(b), 66666666 in b)
# print(time.time() - t1)
# '''
# <class 'list'> True
# 2.4670000076293945
# '''

# print(hash(15), hash('hello'), hash([15, 55]))

b = [15, 85.2, 'hello', 'hello']

print(dir(b))
print(dir(tuple(b)))

c = {'one', tuple(b)}
print(c)
# .__hash__()
# .__eq__()

try:
    hash(b)
    print('hashable')
except Exception as e:
    print('non hashable')





