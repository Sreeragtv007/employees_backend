from django.db import models

# Create your models here.


from django.db import models

class Shift(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.start_time} - {self.end_time}"

class Employee(models.Model):
    name = models.CharField(max_length=100)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    training_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
