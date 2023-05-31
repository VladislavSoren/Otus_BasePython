"""
!!!От базовых классов (BaseOne) нельзя делать инстансы!!!

Можно делать и через raise NotImplementedError, НО
Косяк может не всплыть вплоть до первого использования метода!!!

Если же код нормально покрыт тестами, то это всплывёт, однако всегда
ли тесты есть? Вопрос.

"""


class BaseProduct:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def make_discount(selfself, pcnt):
        raise NotImplementedError('should implement me!')


class NoteBook(BaseProduct):
    pass


note_1 = NoteBook('Note1', 1234)
print(note_1)


