from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.views import View


# Create your views here.
class AddView(View):
    def get(self,req):
        form = DepartmentModelForm()
        context = {'form':form}
        return render(req,'DepartmentApp/add_department.html',context)

    def post(self,req):
        form =DepartmentModelForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('dept_list')

class ListView(View):
    def get(self,req):
        dept_object = Department.objects.all()
        context = {'dept_object':dept_object}
        return render(req,'DepartmentApp/department_list.html',context)

    def post(self, request):
        department = Department.objects.filter(Department_name__icontains=request.POST['searchdata'])
        faculty = department[0].dept_fact.all()
        student = department[0].dept_stud.all()

        template_name = "DepartmentApp/searchinfo.html"
        context = {'department': department, 'faculty': faculty, 'student': student}
        return render(request, template_name, context)


class UpdateView(View):
    def get(self,req,i):
        dept=Department.objects.get(Department_ID=i)
        form = DepartmentModelForm(instance=dept)
        context = {'form':form}
        return render(req,'DepartmentApp/add_department.html',context)

    def post(self,req,i):
        dept = Department.objects.get(Department_ID=i)
        form =DepartmentModelForm(req.POST,instance=dept)
        if form.is_valid():
            form.save()
            return redirect('dept_list')

class DeleteView(View):
    def get(self,req,i):
        dept = Department.objects.get(Department_ID=i)
        dept.delete()
        return redirect('dept_list')

