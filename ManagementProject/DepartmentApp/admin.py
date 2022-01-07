from django.contrib import admin
from .models import *

# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['Department_name','Intake']
admin.site.register(Department,DepartmentAdmin)
