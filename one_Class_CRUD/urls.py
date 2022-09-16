from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('crud/', views.CrudData.as_view(), name='crud'),
    path('<int:id>/del', views.CrudData.as_view(), name='del'),
    path('<int:id>/up', views.CrudData.as_view(), name='up')

]