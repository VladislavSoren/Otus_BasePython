import sys

'''
Mutable объекты это те, у которых можно изменить состояние
Immutable - нельзя

Нужно для:
- оптимизация (экономия памяти, ускорение доступа)
- гарантия неизменяемости состояния объекта (например ключ словаря)
'''

a = [15, 85.2, 'hello']
print(
    type(a),
    id(a),
    sys.getsizeof(a),
    # dir(a)
)

b = (15, 85.2, 'hello',
     15, 85.2, 'hello')
print(
    type(b),
    id(b),
    sys.getsizeof(b),
    # dir(b)
)

# def my_func():
#     pass
#     return response,





