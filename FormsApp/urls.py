from django.urls import path
from FormsApp import views

urlpatterns = [
	path('d/',views.demo),
	path('reg/',views.reg),
]