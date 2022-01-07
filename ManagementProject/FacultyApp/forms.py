from django import forms
from .models import *

class FacultyModelForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = '__all__'