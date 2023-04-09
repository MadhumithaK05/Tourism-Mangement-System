from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login
from aunthentication.models import Members2

# Create your views here.

def home(request):
    return render(request, "aunthentication/index.html")

def signup(request):
    if request.method == "POST":
        
        username = request.POST.get('username')
        email = request.POST['email']
        PhNum = request.POST['phone']
        Pwd = request.POST['pwd']
        ConPwd = request.POST['conpwd']
        
        myuser = Members2(username=username, email=email, phone=int(PhNum), password=Pwd, conpwd=ConPwd)
        
        myuser.save()
        
        messages.success(request, "Successfully Registered")
        return redirect('signin')
        
    return render(request, "aunthentication/signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        Pwd = request.POST.get('pwd')
        
        user = authenticate(username=username, password=Pwd)
        
        if user is not None:
            login(request, user)
            return render(request, "aunthentication/index.html",{'fname':username})
        else:
            messages.error(request, "Bad Credentials")
            return redirect("signin")
        
    return render(request, "aunthentication/signin.html")

def book(request):
    return render(request, "aunthentication/book.html")
