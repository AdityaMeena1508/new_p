
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
        if request.method == 'GET':
            if request.path.endswith("up"):
                return self.put(request, *args, **kwargs)
            elif request.path.endswith("del"):
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

# To Update the data from the database 
# get the data to the update form

    def put(self, request, id, *args, **kwargs):
        if request.method == "GET":
            # breakpoint()
            obj = get_object_or_404(Employee, id = id)
            form=EmployeeForm(request.GET or None, instance=obj)
            return render(request, 'update1.html', {"form":form})  


#  update the data with post request
        if request.method == "POST":
            data = get_object_or_404(Employee, id=id)
            if obj.is_valid():
                obj.save()
                return HttpResponseRedirect('/home1/crud/')

# To delete the data from the db
    def delete(self, request, id):
        data = Employee.objects.get(id=id)
        data.delete()
        return redirect ('/home1/crud')
