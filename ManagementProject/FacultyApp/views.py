from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.views import View


# Create your views here.
class AddView(View):
    def get(self,req):
        form = FacultyModelForm()
        context = {'form':form}
        return render(req,'FacultyApp/add_faculty.html',context)

    def post(self,req):
        form =FacultyModelForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('fact_list')

class ListView(View):
    def get(self,req):
        fact_object = Faculty.objects.all()
        context = {'fact_object':fact_object}
        return render(req,'FacultyApp/faculty_list.html',context)

class UpdateView(View):
    def get(self,req,i):
        fact=Faculty.objects.get(id=i)
        form = FacultyModelForm(instance=fact)
        context = {'form':form}
        return render(req,'FacultyApp/add_faculty.html',context)

    def post(self,req,i):
        fact = Faculty.objects.get(id=i)
        form =FacultyModelForm(req.POST,instance=fact)
        if form.is_valid():
            form.save()
            return redirect('fact_list')

class DeleteView(View):
    def get(self,req,i):
        fact = Faculty.objects.get(id=i)
        fact.delete()
        return redirect('fact_list')

