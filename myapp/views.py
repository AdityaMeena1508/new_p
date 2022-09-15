from http.client import HTTPResponse
from multiprocessing import context    
from django.shortcuts import render,redirect
from .models import Musician

def Emp1(request):
    return render(request, "thoughtwin.html")

def Emp2(request):
    return render(request,'hello.html')

def Emp3(request):
    return render (request, 'contactus.html')

def Registration_form(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        mus=Musician(last_name=lname,first_name = fname)
        
        try:
            mus.save()

        except Exception as e:
            print(e)
    mydata = Musician.objects.all()
    
    return render(request,'list.html',{'mydata' : mydata})
        
    # return render(request, 'list.html')
def delete_data(request, id):
    data = Musician.objects.filter(first_name = id)
    data.delete()
    
    return redirect("/registration_form")

def edit_data(request, id):
    data = Musician.objects.get(first_name = id)
    return render(request,'sys.html',{'first_name' : data}) 


def update_data(request, first_name):

    # damta=Musician.objects.get(first_name = first_name)
    if request.method == "POST": 
        fname=request.POST['fname']
        lname=request.POST['lname']
        data=Musician.objects.get(first_name = first_name)
        data.first_name = fname
        data.last_name = lname
        data.save()  
    #  if request.method=="POST":
        # fname=request.POST['fname']
        # lname=request.POST['lname']
        # mus=Musician(last_name=lname,first_name = fname)
        