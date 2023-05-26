
def get_user_data(usernsme):
    return 'login', 25, 'Moscow', 'junior'


def say_hellow(greeting, name, *args, **kwargs):
    pass


# Параллельное присваивание
user_login, user_age, user_city, *_ = get_user_data('Ivan')  # *_ -> запаковалось
print(user_login, user_age, user_city)
print(_)
print(*_)  # _ -> распаковалось

for _ in range(5):
    pass




