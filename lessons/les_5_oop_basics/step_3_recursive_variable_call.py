'''
Redis - key-value хранилище в оперативке
worker - параллельные процессы (python run.py в разных терминалах)

* Переменная не объявленная в функции будет пытаться рекурсивно найти себя во внешнем мире
* Scopes -области видимости
'''

def say_hello():
    # global user
#    print(f'hello, {user}')
    user = 'Boris'


user = 'Ivan'
print(user)
say_hello()
print(user)