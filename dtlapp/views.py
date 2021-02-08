from django.shortcuts import render

from dtlapp.forms import Userreg
# Create your views here.

def home(request):
	return render(request,'dtlapp/home.html')
def about(request):
	return render(request,'dtlapp/about.html')
def contact(request):
	return render(request,'dtlapp/contact.html')
def dash(request):
	return render(request,'dtlapp/dash.html')
def login(request):
	return render(request,'dtlapp/login.html')
def register(request):
	if request.method == 'POST':
		data=Userreg(request.POST)
		if data.is_valid():
			data.save()
	data=Userreg()
	return render(request,'dtlapp/register.html',{'data':data})