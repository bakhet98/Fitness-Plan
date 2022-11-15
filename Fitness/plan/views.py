from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Exercises


def home(request : HttpRequest):

    return render(request, "plan/base.html")

def exercises(request : HttpRequest):
    if request.method == "POST":
       
        user_exercises = Exercises(name_exercises=request.POST["name_exercises"], day_exercises=request.POST["day_exercises"], counts_exercises = request.POST["counts_exercises"], sets_exercises = request.POST["sets_exercises"], weight_exercises=request.POST["weight_exercises"] )
        user_exercises.save()



    return render(request, "plan/exercisesPlan.html")

def list_exercises(request: HttpRequest):
    if "search" in request.GET:
        exercises = Exercises.objects.filter(title__contains=request.GET["search"])
    else:
        exercises = Exercises.objects.all()

    
    
    

    
    return render(request, "plan/profile.html", {"exercises" : exercises})




