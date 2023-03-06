"""mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from cafe.views import index, coffee, slogan, index2, coffe1, coffe2, coffe3, coffe4, coffe5, coffe6, coffe7, coffe8, coffe9, coffe10, coffe11, mycookie01, mycookie02, mycookie03, mycookie04

urlpatterns = [
    path('admin/', admin.site.urls),
    path('slogan/', slogan),
    
]

urlpatterns += [
    path('', index),
    path('coffee/', coffee),
    path('', index2),
    path('tea/', include('cafe.urls')),
    path('coffee1/', coffe1),
    path('coffee2/', coffe2),
    path('coffee3/', coffe3),
    path('coffee4/', coffe4),
    path('coffee5/', coffe5),
    path('coffee6/', coffe6),
    path('coffee7/', coffe7),
    path('coffee8/', coffe8),
    path('coffee9/<str:pid>/', coffe9),
    path('coffee10/', coffe10),
    path('coffee11/', coffe11),
    path('mycookie01/', mycookie01),
    path('mycookie02/', mycookie02),
    path('mycookie03/', mycookie03),
    path('mycookie04/', mycookie04),
]
