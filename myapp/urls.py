from django.contrib import admin
from django.urls import path
from myapp import views
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Emp1 , name="emp"),
    path('about', views.Emp2, name='aboutus'),
    path('contactus',views.Emp3, name='contactus'),
    path('registration_form', views.Registration_form, name='registration_form')
]