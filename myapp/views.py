from doctest import REPORT_UDIFF
from http.client import HTTPResponse    
from django.shortcuts import render,redirect
from .models import Musician

# Create your views here.

# Create your views here.
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
        mus=Musician(last_name=lname,first_name=fname)
        
        try:
            mus.save()

        except Exception as e:
            print(e)
    mydata = Musician.objects.all()
    
    return render(request,'list.html',{'mydata':mydata})
        
    # return render(request, 'list.html')
def delete_data(request, id):
    data = Musician.objects.filter(pk=id)
    data.delete()
    
    return redirect("/registration_form")

def update_data(request, id):
    data=Musician.objects.get(pk=id)
    breakpoint()
    context={}
    data.save()

    return redirect('/registration_form',context)