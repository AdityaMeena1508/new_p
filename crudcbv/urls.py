from django.contrib import admin
from django.urls import path
from crudcbv import views


urlpatterns = [ 
     path('welcome', views.Create.as_view(), name="home"),
     path('update/<int:id>/', views.Update.as_view(), name='update'),
     path('delete/<int:id>/', views.Delete.as_view(), name='delete')
]