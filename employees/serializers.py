# serializers.py
from rest_framework import serializers
from .models import Employee, Shift, TrainingSchedule

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = '__all__'

class TrainingScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingSchedule
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    shift = ShiftSerializer()
    training_schedule = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ['id', 'name', 'shift', 'training_schedule']
        
    def get_training_schedule(self, obj):
        try:
            return obj.trainingschedule.training_time
        except TrainingSchedule.DoesNotExist:
            return None
