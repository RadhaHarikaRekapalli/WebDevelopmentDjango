from django.urls import path
from Crudapp import views

urlpatterns=[
	path('demo3/',views.demo),
	path('',views.home,name='home'),
	path('addstudent/',views.addstudent,name='addstudent'),
	path('details/',views.details,name='details'),
	path('update/<int:id>/',views.update,name='update'),
	path('delete/<int:id>/',views.delete,name='delete'),
	path('about/',views.about,name='about'),
]