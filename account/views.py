from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def register__view(request):
    form = RegisterForm(request.POST or None)
    
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        
        newUser = User(username = username)
        newUser.set_password(password)
        
        if len(username) < 3:
          messages.error(request, "İstifadəçi adı ən az 3 hərfli olmalıdır!")
        else:
            
            newUser.save()
            messages.success(request, "Siz uğurla qeydiyyatdan keçdiniz!")
            
            login(request, newUser)
            return redirect("home")
        
        
    context = {"form": form}
    messages.info(request, "Sayta daxil olmaq üçün qeydiyyatdan keçməlisiniz!")
    return render(request, "register.html", context)


def login__view(request):
    form = LoginForm(request.POST or None)
    
    context = {"form":form}
    
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        
        user = authenticate(username = username, password = password)
        messages.success(request, f"Siz uğurla sayta daxil oldunuz {username.capitalize()}!")
        
        if user is None:
            return render(request,"login.html", context)
        login(request,user)
        return redirect("home")
    return render(request,"login.html", context)
            
    
        
def logout__view(request):
    logout(request)
    return redirect("home")
