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
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        mus=Musician(last_name=lname,first_name=fname)
        try:
            mus.save()
        except Exception as e:
            print(e)
        mus = Musician.objects.all().order_by('first_name').values()
    return render(request, 'registration_form.html',{'key':'registration'})

def save_registration_data(request):
    
    return redirect(request, 'registration_form.html')