from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Profile

# Create your views here.

def register_user(request : HttpRequest):

    if request.method == "POST":
        #creating the user
        new_user = User.objects.create_user(username=request.POST["username"], email= request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], password=request.POST["password"])
        new_user.save()

        #creating the profile
        



    return render(request, "accounts/register.html")


def login_user(request : HttpRequest):
    msg = ""
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        
        if user:
            login(request, user)
            return redirect("plan:list_exercises")
        else:
            msg = "User Not Found"

    return render(request, "accounts/login.html", {"msg" : msg})


def logout_user(request: HttpRequest):

    logout(request)

    return redirect("plan:list_exercises")

    
