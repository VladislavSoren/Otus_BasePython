from django.core.management import BaseCommand
from faker import Faker

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Hi")
        self.stdout.write("Hello")
        self.stdout.write(
            self.style.WARNING("Hi there"),
        )
        self.stdout.write(
            self.style.SUCCESS("Hello"),
        )