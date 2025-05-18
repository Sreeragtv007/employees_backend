from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, shuffle_training

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employee')

urlpatterns = [
    path('', include(router.urls)),
    path('shuffle/', shuffle_training, name='shuffle-training'),
]
