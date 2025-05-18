# models.py
from django.db import models

class Shift(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.start_time.strftime('%I:%M %p')} - {self.end_time.strftime('%I:%M %p')}"

class Employee(models.Model):
    name = models.CharField(max_length=100)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} (Shift: {self.shift})"

class TrainingSchedule(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    training_time = models.TimeField()

    def __str__(self):
        return f"{self.employee.name} - Training: {self.training_time.strftime('%I:%M %p')}"
