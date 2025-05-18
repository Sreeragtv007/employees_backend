from django.core.management.base import BaseCommand
from employees.models import Employee, Shift
from faker import Faker
import random
from datetime import time

class Command(BaseCommand):
    help = 'Seed the database with fake employees and shifts'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Clear old data
        Employee.objects.all().delete()
        Shift.objects.all().delete()

        # Define shifts
        shift_definitions = [
            (time(8, 30), time(17, 30), 100),
            (time(14, 0), time(23, 0), 50),
            (time(0, 0), time(9, 0), 20),
        ]

        shifts = []
        for start, end, count in shift_definitions:
            shift = Shift.objects.create(start_time=start, end_time=end)
            shifts.append((shift, count))

        # Create employees
        for shift, count in shifts:
            for _ in range(count):
                Employee.objects.create(
                    name=fake.name(),
                    shift=shift
                )

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
