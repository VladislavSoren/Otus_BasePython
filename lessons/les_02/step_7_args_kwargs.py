SAY_HI = True

def say_hello(user_name: str, greeting='', start_word='hello') -> None:
    print(start_word, user_name, greeting)


#args = ('a.andreeev', 'have a very good day', 'hi',)
args = ('a.andreeev',)
say_hello(*args)

kwargs = {
    # 'user_name': 'a.andreeev',
    'greeting': 'have a very good day',
    # 'start_word': 'hi',
}

if SAY_HI:
    kwargs['start_word'] = 'hi'

say_hello(*args, **kwargs)

