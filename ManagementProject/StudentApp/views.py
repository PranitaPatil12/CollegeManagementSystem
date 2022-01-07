from django.shortcuts import render,redirect
from StudentApp.models import Student
from .forms import *
from django.views import View


# Create your views here.
class AddView(View):
    def get(self,req):
        form = StudentModelForm()
        context = {'form':form}
        return render(req,'StudentApp/add_student.html',context)

    def post(self,req):
        form =StudentModelForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('stud_list')

class ListView(View):
    def get(self,req):
        stud_object = Student.objects.all()
        context = {'stud_object':stud_object}
        return render(req,'StudentApp/student_list.html',context)

class UpdateView(View):
    def get(self,req,i):
        stud=Student.objects.get(id=i)
        form = StudentModelForm(instance=stud)
        context = {'form':form}
        return render(req,'StudentApp/add_student.html',context)

    def post(self,req,i):
        stud = Student.objects.get(id=i)
        form =StudentModelForm(req.POST,instance=stud)
        if form.is_valid():
            form.save()
            return redirect('stud_list')

class DeleteView(View):
    def get(self,req,i):
        stud = Student.objects.get(id=i)
        stud.delete()
        return redirect('stud_list')

