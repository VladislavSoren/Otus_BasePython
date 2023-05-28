'''

Class methods don’t need a class instance.
They can’t access the instance (self) but they have access to the class itself via cls.

@classmethod – это метод, который получает класс в качестве неявного первого аргумента,
точно так же, как обычный метод экземпляра получает экземпляр.
Это означает, что вы можете использовать класс и его свойства внутри этого метода,
а не конкретного экземпляра.

Проще говоря, @classmethod – это обычный метод класса, имеющий доступ ко всем атрибутам класса,
через который он был вызван. Следовательно, classmethod – это метод, который привязан к классу,
а не к экземпляру класса.

'''


class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __str__(self):
        return f'Pizza({self.ingredients!r})'

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])


if __name__ == '__main__':
    # print(repr(Pizza(['cheese', 'tomatoes'])))

    # print(repr(Pizza.margherita()))
    Pizza_margherita = Pizza.margherita()
    print(repr(Pizza_margherita), str(Pizza_margherita), Pizza_margherita.ingredients)

    # print(repr(Pizza.prosciutto()))
    Pizza_prosciutto = Pizza.prosciutto()
    print(repr(Pizza_prosciutto), str(Pizza_prosciutto), Pizza_prosciutto.ingredients)