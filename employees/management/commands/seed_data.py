from django.core.management.base import BaseCommand
from employees.models import Employee
from faker import Faker
from datetime import time
from employees.models import Employee


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        fake = Faker()

        for i in range(100):
            Employee.objects.create(
                name=fake.name(), available_from=time(8, 30), available_to=time(17, 30))

        for i in range(100, 150):
            Employee.objects.create(
                name=fake.name(), available_from=time(14, 0), available_to=time(23, 0))

        for i in range(150, 170):
            Employee.objects.create(
                name=fake.name(), available_from=time(0, 0), available_to=time(9, 0))

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
