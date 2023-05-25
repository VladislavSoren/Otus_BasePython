
'''
SRP
Single responsibility principle) обозначает, что каждый объект должен иметь одну обязанность
и эта обязанность должна быть полностью инкапсулирована в класс.
Все его сервисы должны быть направлены исключительно на обеспечение этой обязанности.
'''

def say_hello(user_name: str, greeting='', start_word='hello', **kwargs) -> None:
    print(kwargs)
    print(start_word, user_name, greeting)

    validate = kwargs.get('validate')
    print(validate)


args = ('a.andreeev',)
# say_hello(*args, validate=True)
say_hello(*args)


