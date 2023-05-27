'''
Использование global - коварная практика
к ней лучше прибегать только при крайней необходимости, а лучше
вообще не прибегать
'''

def say_hello():
    global user
    print(f'hello, {user}')
    user = 'Boris'


user = 'Ivan'
print(user)
say_hello()
print(user)