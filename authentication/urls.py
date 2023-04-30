from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index.html', views.home, name="home"),
    path('signup.html', views.signup, name="signup"),
    path('signin.html', views.signin, name="signin"),
    path('adminlogin.html', views.adminlogin, name="adminlogin"),
    path('book.html', views.book, name="book"),
    path('custom.html', views.custom, name="custom"),
    path('trans.html', views.trans, name="trans"),
    path('notcomplete.html', views.com, name="com"),
    #path('notcomplete.html', views.completed, name="completed"),
    path('signout',views.signout, name="signout"),
]
