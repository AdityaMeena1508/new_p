
from multiprocessing import context
from django.shortcuts import render,redirect,HttpResponseRedirect, get_object_or_404
from .models import Employee
from .form import EmployeeForm
from django.views import View
# Create your views here.

class CrudData(View):

# To channge the route of the urls
# run to get the data from the urls

    
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET' :
            if request.path.endswith("up"):
                return self.put(request, *args, **kwargs)
            if request.path.endswith("del"):
                return self.delete(request, *args, **kwargs)
            return self.get(request, *args, **kwargs)
# to run on post the data
        elif request.method == 'POST':
            if request.path.endswith("up"):
                return self.put(request, *args, **kwargs)
            return self.post(request, *args, **kwargs)

            
# To add the data in the database
    def get(self, request ,*args, **kwargs):
        data= Employee.objects.all()
        obj = EmployeeForm()
        context={'form':obj,
        'data':data,
        }
        return render (request, "home1.html",context)


# To retrieve the data from the database
    def post(self, request, *args, **kwargs):
        data =EmployeeForm(request.POST)
        if data.is_valid():
            data.save()
        return redirect('/home1/crud')
    
    def put(self, request, id):
        if request.method == 'POST':
            obj=get_object_or_404(Employee,id=id)
            form=EmployeeForm(request.POST,instance=obj)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect('/home1/crud/')
        
        if request.method == 'GET':
            obj=Employee.objects.get(id=id)
            form=EmployeeForm(instance=obj)
            return render(request,'update1.html',{'form':form})


        # def put(self,request,id):
        # if request.method == 'POST':
        #     data11=get_object_or_404(Student,id=id)
        #     data21=StudentForm(request.POST,instance=data11)
        #     if data21.is_valid():
        #         data21.save()
        #     return HttpResponseRedirect('/CRUD3/home/')
        # if request.method == 'GET':
        #     data11=Student.objects.get(id=id)
        #     data12=StudentForm(instance=data11)
        #     return render(request,'UPD.html',{'form':data12})

# To delete the data from the db
    def delete(self, request, id):
        data = Employee.objects.get(id=id)
        data.delete()
        return redirect ('/home1/crud')
