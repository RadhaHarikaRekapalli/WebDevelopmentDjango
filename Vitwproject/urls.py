"""Vitwproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('greet/',views.sample),
    path('myself/',views.display),
    path('paragraph/',views.para),
    path('apssdc/',views.browser),
    path('stringvalue/<str:name>/<int:num>/',views.stringvalueex),
    path('durl/<str:name>/<int:num>/',views.descript),
    path('samplehtml/',views.samplehtmlex,name='sample'),
    path('demo/',views.htmlexcss,name=''),
    path('demo2/',views.external,name=''),
    path('bootex/',views.bootstrapexp,name=''),
    path('loginpage/',views.login,name=''),
    path('registerpage/',views.register,name=''),
    path('',include('Crudapp.urls')),
    path('forms/',include('FormsApp.urls')),
    path('dtlapp/',include('dtlapp.urls')),
]
