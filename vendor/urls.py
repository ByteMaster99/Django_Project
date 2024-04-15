"""
URL configuration for vendor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from user_detail import views as user_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('Register',user_views.Register,name='Register'),
    path('Vendormodel',user_views.Vendormodel,name="Vendormodel"),
    path('addressmodel',user_views.addressmodel,name="addressmodel"),
    path('contactmodel',user_views.contactmodel,name="contactmodel"),
    path('getregister',user_views.getregister,name="getregister"),
    path('getaddress',user_views.getaddress,name="getaddress"),
    path('getcontact',user_views.getcontact,name="getcontact"),
    path("getvendor",user_views.getvendor,name="getvendor"),
    path('Q_register',user_views.Q_register,name="Q_register"),
    path('Q_address',user_views.Q_address,name="Q_address"),
    path('Q_contact',user_views.Q_contact,name="Q_contact"),
    path("Q_vendor",user_views.Q_vendor,name="Q_vendor"),
    path("display_register/<pk>",user_views.display_register,name="display_register"),
    path("display_address/<pk>",user_views.display_address,name="display_address"),
    path("display_contact/<pk>",user_views.display_contact,name="display_contact"),
    path("display_vendor/<pk>",user_views.display_vendor,name="display_vendor"),    
    path("index",user_views.index,name="index"),
    path("gregister",user_views.gregister,name="gregister"),
    path("delete_register/<pk>",user_views.delete_register,name="delete_register"),
    path("delete_address/<pk>",user_views.delete_address,name="delete_address"),
    path("delete_contact/<pk>",user_views.delete_contact,name="delete_contact"), 
    path("delete_vendor/<pk>",user_views.delete_vendor,name="delete_vendor"), 
    path("login",user_views.login,name="login"),
    path("find_register",user_views.find_register,name="find_register"),


    
    

    









]
