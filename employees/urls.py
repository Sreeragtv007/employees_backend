from django.urls import path, include
from .views import shuffle_training, employee_list,shuffle_training2


urlpatterns = [

    path('shuffle/', shuffle_training, name='shuffle-training'),
    path('employees/', employee_list, name='employee_list'),
    path('shuffle2/', shuffle_training2, name='shuffle_training2'),
]


