__all__ = ("fake",)

from faker import Faker

Faker.seed('test_1')

fake = Faker()
