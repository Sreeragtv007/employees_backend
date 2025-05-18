import random
from datetime import time, datetime, timedelta

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer


# Employee List ViewSet
class EmployeeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# Shuffle Training API
@api_view(['POST'])
def shuffle_training(request):
    # Define available training slots (every hour from 8am to 5pm)
    start_hour = 8
    end_hour = 18
    slots = [time(hour=h) for h in range(start_hour, end_hour)]

    # Empty all existing training times
    Employee.objects.update(training_time=None)

    employees = list(Employee.objects.all())
    random.shuffle(employees)

    # Group employees by availability
    slot_batches = {slot: [] for slot in slots}

    for emp in employees:
        # Find slots where employee is available
        available_slots = [
            slot for slot in slots
            if emp.available_from <= slot < emp.available_to
        ]
        random.shuffle(available_slots)

        # Try to assign to a random available slot with less than 25 people
        assigned = False
        for slot in available_slots:
            if len(slot_batches[slot]) < 25:
                slot_batches[slot].append(emp)
                emp.training_time = slot
                emp.save()
                assigned = True
                break

    return Response({"status": "Training shuffled"})
