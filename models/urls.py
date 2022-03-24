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
from django.contrib import admin
from django.urls import path, include
from payment.views import (
    CreatCheckoutSessionView, 
    ProductLandingView,
    PaymentFails,
    PaymentSucces,
    RemitaPayment,
    PagaPayment,
    FlutterPayView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('example.urls')),
    path('create-checkout-session/<int:pk>/', CreatCheckoutSessionView.as_view(), name = 'create_checkout'),
    path('payment/<int:pk>/', ProductLandingView.as_view(), name = 'landing_page'),
    path('success/', PaymentSucces.as_view(), name = 'success'),
    path('failure/', PaymentFails.as_view(), name = 'failure'),
    path('remita_gateway/', RemitaPayment.as_view(), name = 'remita'),
    path('paga_gateway/', PagaPayment.as_view(), name ='paga'),
    path('fluter_gateway/', FlutterPayView.as_view(), name = 'fluter'),


]
