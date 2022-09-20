from email.policy import default
from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from .models import Student
from .forms import StudentForm
from Generic_CRUD import forms
# Create your views here.

class StudentDetailView(DetailView):
    model = Student
    template_name = "ho.html"


class StudentListView(ListView):
    model = Student
    template_name = 'Student_list.html'
    context_object_name = "student"
    
    def get_queryset(self):
      return Student.objects.all()


