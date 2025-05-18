from django.core.management.base import BaseCommand
from employees.models import Employee
from faker import Faker
import random
from datetime import time
from employees.models import Employee

class Command(BaseCommand):
    help = 'Seed the database with fake employees and shifts'

    def handle(self, *args, **kwargs):
        


# Create 100 employees (8:30 AM to 5:30 PM)
        for i in range(100):
            Employee.objects.create(
                name=f"Emp{i+1}", available_from=time(8, 30), available_to=time(17, 30))

        # 50 employees (2 PM to 11 PM)
        for i in range(100, 150):
            Employee.objects.create(
                name=f"Emp{i+1}", available_from=time(14, 0), available_to=time(23, 0))

        # 20 employees (12 AM to 9 AM)
        for i in range(150, 170):
            Employee.objects.create(
                name=f"Emp{i+1}", available_from=time(0, 0), available_to=time(9, 0))

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
