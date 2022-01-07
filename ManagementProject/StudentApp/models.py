from django.db import models
from DepartmentApp.models import Department

# Create your models here.
class Student(models.Model):
    department = models.ForeignKey(Department,related_name='dept_stud',on_delete=models.CASCADE)
    Roll_No = models.IntegerField()
    Name = models.CharField(max_length=32)
    Marks = models.FloatField()

    def __str__(self):
        return f"{self.department}, {self.Roll_No},{self.Name},{self.Marks}"
