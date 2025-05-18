from django.urls import path, include
from .views import shuffle_training, employee_list


urlpatterns = [

    path('shuffle/', shuffle_training, name='shuffle-training'),
    path('employees/', employee_list, name='employee_list'),
]
