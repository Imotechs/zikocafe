"""models URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from django.contrib import admin
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from .views import AddJobView, Register, about

urlpatterns = [
    path('',views.home, name = 'home'),
    path('add_todo/',views.add_todo, name = 'add_todo'),
    path('delete_todo/<int:todo_id>/',views.delete_todo, name = 'delete_todo'),
    path('add_job_done/', AddJobView.as_view(), name = 'addjob'),
    path('register/', views.Register, name ='register'),
    path('about/', views.about, name= 'about'),
    path('loggout/', auth_views.LogoutView.as_view(template_name = 'example/logout.html'), name = 'logout'),
    path('loggin/', auth_views.LoginView.as_view(template_name = 'example/login.html'), name = 'login'),
  path('make_payment/<int:pk>/', views.allPaymentView, name = 'makepayment'),
]

