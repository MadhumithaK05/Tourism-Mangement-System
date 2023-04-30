from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from authentication.models import Customers
from authentication.models import Transaction
from authentication.forms import place
from tour import settings

# Create your views here.

def home(request):
    return render(request, "authentication/index.html")

def signup(request):
    if request.method == "POST":
        
        username = request.POST['username']
        email = request.POST['email']
        phone= request.POST['phone']
        password = request.POST['password']
        #conpwd = request.POST['conpwd']
        
        myuser = User.objects.create_user(username=username, email=email, password=password)
        myuser.save()
        
        myuser1 = Customers(username=username, email=email, password=password)
        myuser1.phone=int(phone)
        myuser1.save()
        
        messages.success(request, "Successfully Registered")
        return redirect('signin')
        
    return render(request ,"authentication/signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return render(request, "authentication/index.html",{'fname':username})
        else:
            messages.error(request, "Bad Credentials")
            return redirect("signin")
        
    return render(request, "authentication/signin.html")

def adminlogin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        if username=="admin" and password=="rec":
            return render(request, "authentication/custom.html")
        else:
            messages.error(request, "Bad Credentials")
            return redirect("adminlogin")
        
    return render(request, "authentication/adminlogin.html")

def book(request):
    if request.method == "POST":
        username = request.POST["username"]
        phone=request.POST["phone"]
        place=request.POST.get('City','')
        number_pass=request.POST["mem"]
        price=request.POST["amt1"]
        '''form = place(request.POST)
        form.save()'''
        trans=Transaction(username=username, phone=phone, place=place, number_pass=number_pass, price=price)
        trans.save()
        messages.success(request, "inserted {} successfully".format(place))
    return render(request, "authentication/book.html")

def custom(request):
    info=Customers.objects.all()
    data= {
    "cust": info
}
    return render(request, "authentication/custom.html",data)

def trans(request):
    tinfo= Transaction.objects.all()
    data= {
    "tr": tinfo
}
    return render(request, "authentication/trans.html",data)

def com(request):
    tinfo= Transaction.objects.filter(completed=False)
    data= {
    "tr": tinfo
}
    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_items')
        for i in selected_ids:
            transactions = Transaction.objects.filter(phone=i)
            transactions.update(completed=True)
        messages.success(request, "updated successfully")
        return render(request, "authentication/notcomplete.html",data)

    return render(request, "authentication/notcomplete.html",data)

def signout(request):
    logout(request)
    messages.success(request,"Loged out Successfully")
    return redirect('home')