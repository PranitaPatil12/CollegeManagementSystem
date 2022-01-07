from django.db import models

# Create your models here.
class Department(models.Model):
    Department_ID = models.IntegerField(primary_key=True)
    Department_name = models.CharField(max_length=100,unique=True)
    Intake = models.IntegerField()

    def __str__(self):
        return f"{self.Department_name}"
