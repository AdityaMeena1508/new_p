from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.views.generic.base import View
from crudcbv.form import UserForm
from .models import User


# Create your views here.
class Create(View):
    def get(self, request):
        data = User.objects.all()
        obj = UserForm
        context={
            'form':obj,
            'data':data,
        }
        return render(request, "home.html", context)
    
    def post(self, request):
        data = UserForm(request.POST)
        if data.is_valid():
            data.save()
        return redirect('/home/welcome')



class Update(View):

    def get(self, request, id): 
        data = User.objects.get(id=id)
        obj = UserForm(instance =data, )
        print(data)
        return render(request,'update.html',{'id':data})



class Update(View):
    def get(self, request, id):
        data= User.objects.get(pk=int(request.GET["q"]))
        return render(request, 'update.html', {"data":data})

    def post(self, request, id):

        data =UserForm(request.POST)
        if data.is_valid():
            data.save()
        return HttpResponseRedirect("/home/welcome")

    # def put(self, request, id): 
    #     data = User.objects.get(id=id)
    #     # obj = UserForm(instance = , )
    #     print(data)
    #     return render(request,'update.html',{'id':data})    

    
class Delete(View):
    def get (self, request, id ):
        data= User.objects.get(id=id)
        data.delete()
        return HttpResponseRedirect("/home/welcome")
        
