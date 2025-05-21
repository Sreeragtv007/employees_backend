from collections import defaultdict
import random
from datetime import time
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import status
from collections import defaultdict


@api_view(['GET'])
def employee_list(request):
    employees = Employee.objects.all()

    # for emp in employees:
    #     if not emp.available_from <= emp.training_time < emp.available_to:
    #         print(emp.name)
    #         print('employees not in the sift time')
    # for i in range(8, 18):
    #     obj = Employee.objects.filter(training_time=time(i, 0)).count()
    #     print('-------------------------')
    #     print(obj)

    emp = Employee.objects.filter(training_time=None).count()
    print('--- training none----')
    print(emp)
    serializer = EmployeeSerializer(employees, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def shuffle_training(request):
    start_hour = 8
    end_hour = 18
    slots = [time(hour=h) for h in range(start_hour, end_hour)]

    Employee.objects.update(training_time=None)

    employees = list(Employee.objects.all())
    random.shuffle(employees)

    slot_batches = {slot: [] for slot in slots}

    for emp in employees:

        available_slots = [
            slot for slot in slots
            if emp.available_from <= slot < emp.available_to
        ]
        # random.shuffle(available_slots)

        for slot in available_slots:
            if len(slot_batches[slot]) < 20:
                slot_batches[slot].append(emp)
                emp.training_time = slot
                emp.save()
                break

    return Response({"status": "Training shuffled"}, status=status.HTTP_200_OK)



@api_view(['POST'])
def shuffle_training2(request):
    start_hour = 8
    end_hour = 18
    slots = [time(hour=h) for h in range(start_hour, end_hour)]

    Employee.objects.update(training_time=None)

    employees = list(Employee.objects.all())
    random.shuffle(employees)

    slot_counts = defaultdict(int)

    assigned_employees = []

    for emp in employees:
        for slot in slots:
            if emp.available_from <= slot < emp.available_to and slot_counts[slot] < 20:
                emp.training_time = slot
                slot_counts[slot] += 1
                assigned_employees.append(emp)
                break

    Employee.objects.bulk_update(assigned_employees, ['training_time'])

    return Response({"status": "Training shuffled"}, status=status.HTTP_200_OK)
