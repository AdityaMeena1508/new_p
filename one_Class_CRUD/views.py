
from multiprocessing import context
from django.shortcuts import render,redirect,HttpResponseRedirect, get_object_or_404
from .models import Employee
from .form import EmployeeForm
from django.views import View
# Create your views here.

class CrudData(View):


    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            if request.path.endswith("up"):
                return self.put(request, *args, **kwargs)
            elif request.path.endswith("del"):
                return self.delete(request, *args, **kwargs)
            return self.get(request, *args, **kwargs)
        elif request.method == 'POST':
            if request.path.endswith("up"):
                return self.put(request, *args, **kwargs)
            return self.post(request, *args, **kwargs)

    def get(self, request ,*args, **kwargs):
        data= Employee.objects.all()
        obj = EmployeeForm()
        context={'form':obj,
        'data':data,
        }
        return render (request, "home1.html",context)

    def post(self, request, *args, **kwargs):
        data =EmployeeForm(request.POST)
        if data.is_valid():
            data.save()
        return redirect('/home1/crud')
    
    def put(self, request, id, *args, **kwargs):
        obj = get_object_or_404(Employee, id = id)
        form=EmployeeForm(request.GET or None, instance=obj)
        if request.method == "POST":
            data = get_object_or_404(Employee, id=id)
            if obj.is_valid():
                obj.save()
                return HttpResponseRedirect('/home1/crud/')
        return render(request, 'update1.html', {"form":form}) 

    def delete(self, request, id):
        data = Employee.objects.get(id=id)
        data.delete()
        return redirect ('/home1/crud')
