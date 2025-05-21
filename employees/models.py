from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    available_from = models.TimeField(blank=True, null=True)
    available_to = models.TimeField(blank=True, null=True)
    training_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    
