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
        user_profile = Profile(user=new_user, age=request.POST["age"], address=request.POST["address"])
        user_profile.save()



    return render(request, "accounts/register.html")


def login_user(request : HttpRequest):
    msg = ""
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        
        if user:
            login(request, user)
            return redirect("blogApp:list_posts")
        else:
            msg = "User Not Found , check your credentials"

    return render(request, "accounts/login.html", {"msg" : msg})


def logout_user(request: HttpRequest):

    logout(request)

    return redirect("plog:list_exercises")

    
