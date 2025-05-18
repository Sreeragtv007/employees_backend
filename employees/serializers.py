from rest_framework import serializers
from .models import Employee, Shift

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    shift = ShiftSerializer()

    class Meta:
        model = Employee
        fields = ['id', 'name', 'shift', 'training_time']
