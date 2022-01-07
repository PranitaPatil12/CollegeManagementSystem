from django.db import models
from DepartmentApp.models import Department

class Faculty(models.Model):
    department = models.ManyToManyField(Department,related_name='dept_fact')
    Faculty_Name = models.CharField(max_length=70)
    Faculty_Salary = models.FloatField()