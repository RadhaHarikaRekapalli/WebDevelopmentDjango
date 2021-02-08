from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def sample(request):
	return HttpResponse("<h1>Welcome to django session</h1>")
def display(request):
	return HttpResponse("<center>This is display method</center>")
def para(request):
	return HttpResponse("<p>Django is a web application framework written in Python programming language. By using Django, we can build web applications in very less time. ... Django is designed in such a manner that it handles much of configure things automatically, so we can focus on application development only.</p>")
def browser(request):
	return HttpResponse("<center><h1>Django Session</h1></center><br></br><h2>This is Harika</h2><br></br><p>Welcome to the django session.Django is a web application framework written in Python programming language. By using Django, we can build web applications in very less time. ... Django is designed in such a manner that it handles much of configure things automatically, so we can focus on application development only.</p><br></br><h2>Organized By:</h2><br></br><h5>APSSDC</h5><br></br><h5>VITW</h5>")
def stringvalueex(request,name,num):
	return HttpResponse("Hellooooo.....%d"%num+name)
def descript(request,name,num):
	return HttpResponse("Hello...."+name+"<br></br>Age is:%d"%num)
def samplehtmlex(request):
	return render(request,'student/sample.html')
def htmlexcss(request):
	return render(request,'student/demo.html')
def external(request):
	return render(request,'student/demo2.html')
def bootstrapexp(request):
	return render(request,'student/bootstrapexp.html')
def login(request):
	return render(request,'student/login.html')
def register(request):
	if request.method == 'POST':
		Fname = request.POST.get('fname')
		Lname = request.POST.get('lname')
		Username = request.POST.get('username')
		Rollno = request.POST.get('rollnos')
		Email = request.POST.get('email')
		Password = request.POST.get('password')
		# Cpassword = request.POST.get('cpassword')
		Mobile = request.POST.get('mobile')
		#print(Fname,Lname,Email)
		return render(request,'student/details.html',{'Fname':Fname,'Lname':Lname,'Username':Username,'Rollno':Rollno,'Email':Email,'Password':Password,'Mobile':Mobile})
	return render(request,'student/register.html')