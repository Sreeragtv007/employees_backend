# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee, TrainingSchedule
from .serializers import EmployeeSerializer
from datetime import time, timedelta, datetime
import random

class EmployeeListView(APIView):
    def get(self, request):
        employees = Employee.objects.all().prefetch_related('shift')
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

class ShuffleTrainingView(APIView):
    def post(self, request):
        employees = list(Employee.objects.all())
        random.shuffle(employees)

        slots = [datetime.strptime(f"{hour}:00", "%H:%M").time() for hour in range(8, 18)]
        current_slot_idx = 0
        batch_size = 0
        batch_limit = random.randint(10, 25)

        for employee in employees:
            if batch_size >= batch_limit:
                current_slot_idx = (current_slot_idx + 1) % len(slots)
                batch_size = 0
                batch_limit = random.randint(10, 25)

            training_time = slots[current_slot_idx]

            TrainingSchedule.objects.update_or_create(
                employee=employee,
                defaults={"training_time": training_time}
            )

            batch_size += 1

        return Response({"status": "success", "message": "Training times shuffled."})
