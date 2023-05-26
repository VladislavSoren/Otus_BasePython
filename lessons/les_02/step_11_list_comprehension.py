import time

'''
list !comprehension! python (СПИСКОВОЕ ВКЛЮЧЕНИЕ)

List comprehension offers a shorter syntax
when you want to create a new list based on the values of an existing list.

Плюшки:
* Прирост в скорости!
'''

users = ['i.ivanov', 'a.andreeev', 's.sergeev']

print([user + ' hi' for user in users if not user.startswith('a')])

compreh_list = {user + ' 123': 1 for user in users }
print(compreh_list)

#########################################
# Сравнение скорости формирования списков
#########################################
users = [f'{i}' for i in range(1000000)]

t1 = time.time()
simple_list = []
for user in users:
    if not user.startswith('1'):
        simple_list.append(user + '123')
print(time.time() - t1)

t1 = time.time()
compreh_list = [user + ' 123' for user in users if not user.startswith('1')]
print(time.time() - t1)


