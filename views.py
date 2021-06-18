from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return HttpResponse("Hi Good Evening to All...")

def htmltag(y):
	return HttpResponse("<h2>Hi Welcome to APSSDC</h2>")

def usernameprint(request,uname):
	return HttpResponse("<h2>Hi Welcome <span style='color:green'>{}</span></h2>".format(uname))

def usernameage(request,un,ag):
	return HttpResponse("<h3 style='text-align:center;background-color:green'>My name is <span style='color:yellow'>{}</span> and my age is: <span style='color:red'>{}</span></h3>".format(un,ag))

def empdetails(request,eid,ename,eage):
	return HttpResponse("<script>alert('Hi Welcome {}')</script><h3>Hi Welcome {} and your age is {} and your id is {}</h3>".format(ename,ename,eage,eid))

def htm(request):
	return render(request,'html/basics.html')

def ytname(request,name):
	return render(request,'html/ytname.html',{'n':name})

def empname(request,id,name):
	k = {'i':id,'n':name}
	return render(request,'html/ehtml.html',k)

def studentdetails(request):
	return render(request,'html/stud.html')

def internaljs(request):
	return render(request,'html/internaljs.html')

def myform(request):
	if request.method=="POST":
		#print(request.POST)
		uname = request.POST['uname']
		rollno = request.POST['rollno']
		email = request.POST['email']
		print(uname,rollno,email)
		data = {'username':uname,'rno':rollno,'emailid':email}
		return render(request,'html/display.html',data)
	return render(request,'html/form.html')

def bootstrap(request):
	return render(request,'html/boot.html')

def Registration(request):
	if request.method=="POST":
		fname = request.POST['fname']
		lname = request.POST['lname']
		rollno = request.POST['rollno']
		email = request.POST['email']
		phoneno = request.POST['phoneno']
		print(fname,lname,rollno,email,phoneno)
		data = {'firstname':fname,'lastname':lname,'rno':rollno,'emailid':email,'pno':phoneno}
	return render(request,'html/Registration.html')

	

