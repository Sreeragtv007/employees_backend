from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from .utils import schedule_trainings
# Create your views here.



class test(APIView):
    def get(self,request):
        
        return Response("testt")
    
    
    


@api_view(['GET'])
def list_employees(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def shuffle_training_schedule(request):
    schedule_trainings()
    return Response({'message': 'Training schedule updated.'})
