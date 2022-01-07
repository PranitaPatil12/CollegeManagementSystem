from django.contrib import admin
from .models import *
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['department','Roll_No','Name','Marks']
admin.site.register(Student,StudentAdmin)