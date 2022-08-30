from django.shortcuts import render

# Create your views here.

# Create your views here.
def Emp1(request):
   
    return render(request, "thoughtwin.html")

def Emp2(request):


    return render(request,'hello.html')

def Emp3(request):

    return render (request, 'contactus.html')

def Registration_form(request):
    # if request.method=="POST":
    #     fname=request.POST['firstname']
    #     lname=request.POST['lastname']
    #     mus=Musician(first_name=fname, last_name=lname)
    #     mus.save()

    return render(request, 'registration_form.html',{'key':'registration'})
