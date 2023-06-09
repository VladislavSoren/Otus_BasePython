def say_hello(user_name, greeting='', start_word='hello'):
    print(start_word, user_name, greeting)


def greet_users(users):
    for user_name in users:
        say_hello(user_name)


say_hello('a.andreeev')
say_hello('a.andreeev', 'have a very good day!')
say_hello('a.andreeev', 'have a very good day!', 'hi')
say_hello('a.andreeev', 'hi', 'have a very good day!')
# kwargs keyword arguments
say_hello('a.andreeev', start_word='hi', greeting='have a very good day!')
say_hello(user_name='a.andreeev', start_word='hi', greeting='have a very good day!')