from django.contrib import admin
from django.urls import path
from myapp import views
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Emp1 , name="emp"),
    path('about', views.Emp2, name='aboutus'),
    path('contactus',views.Emp3, name='contactus'),
    path('registration_form', views.Registration_form, name='registration_form'),
    path('delete/<str:id>/',views.delete_data,name='delete'),
    path('edit/<str:id>/', views.edit_data,name='edit'), 
    path('update/<str:first_name>',views.update_data,name='update'),  
    # path('list_data', views.save_registration_data, name='list_data'),
    
]