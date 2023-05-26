
def get_user_data(usernsme):
    return 'login', 25


# Параллельное присваивание
user_login, user_age = get_user_data('Ivan')
print(user_login, user_age)