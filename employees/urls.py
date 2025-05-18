
from django.contrib import admin
from django.urls import path
from .views import EmployeeListView,ShuffleTrainingView
urlpatterns = [
    path('employees/', EmployeeListView.as_view(), name='employee-list'),
    path('shuffle/', ShuffleTrainingView.as_view(), name='shuffle-training'),
]
