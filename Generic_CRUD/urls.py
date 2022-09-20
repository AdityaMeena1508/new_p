from django.contrib import admin
from django.urls import path
from Generic_CRUD import views


urlpatterns = [
    
   path ('<int:pk>/', views.StudentDetailView.as_view()),
   path('', views.StudentListView.as_view()),
   path('',views.StudentCreateView.as_view())
]