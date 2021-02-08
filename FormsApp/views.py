from django.shortcuts import render
from django.http import HttpResponse
from FormsApp.forms import StudentForm

# Create your views here.
def demo(request):
	return HttpResponse('<center><h3>I am from FormsApp</h3></center>')
def reg(request):
	if request.method == 'POST':
		form = StudentForm(request.POST)
		form.save()
		return HttpResponse('Data inserted using Forms....')
	form=StudentForm()
	return render(request,'FormsApp/reg.html',{'form':form})