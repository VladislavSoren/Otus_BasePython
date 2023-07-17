from django.core.management import BaseCommand
from faker import Faker

fake = Faker(locale="ru_Ru")

Faker.seed('seed_1')


class Command(BaseCommand):
    def handle(self, *args, **options):
        for _ in range(1):
            self.stdout.write(
                fake.pystr(
                    min_chars=10,
                    max_chars=10,
                    prefix="V_",
                    suffix="-V",
                )
            )
            self.stdout.write(fake.phone_number())

            self.stdout.write(fake.name())



