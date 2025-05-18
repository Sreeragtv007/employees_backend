from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'available_from',
                    'available_to', 'training_time')
    search_fields = ('name',)
    ordering = ('id',)
