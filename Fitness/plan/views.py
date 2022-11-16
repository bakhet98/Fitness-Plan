from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Exercises , Food


def home(request : HttpRequest):

    return render(request, "plan/base.html")

def exercises(request : HttpRequest):
    if request.method == "POST":
       
        user_exercises = Exercises(name_exercises=request.POST["name_exercises"], day_exercises=request.POST["day_exercises"], counts_exercises = request.POST["counts_exercises"], sets_exercises = request.POST["sets_exercises"], weight_exercises=request.POST["weight_exercises"] )
        user_exercises.save()

        return redirect("plan:list_exercises")



    return render(request, "plan/exercisesPlan.html")

def list_exercises(request: HttpRequest):
    if "search" in request.GET:
        exercises = Exercises.objects.filter(title__contains=request.GET["search"])
    else:
        exercises = Exercises.objects.all()

    if "search" in request.GET:
        meal = Food.objects.filter(title__contains=request.GET["search"])
    else:
        meal = Food.objects.all()
    
    return render(request, "plan/profile.html", {"exercises" : exercises, "meals" : meal})

def meal(request : HttpRequest):
    if request.method == "POST":
       
        user_meal = Food(meal=request.POST["meal"], colres=request.POST["colres"])
        user_meal.save()

    return render(request, "plan/foodplan.html")


def list_food(request: HttpRequest):
    if "search" in request.GET:
        meal = Food.objects.filter(title__contains=request.GET["search"])
    else:
        meal = Food.objects.all()

    
    
    return render(request, "plan/profile.html", {"meal" : meal})

def plansAvailable(request : HttpRequest):

    return render(request, "plan/plansAvailable.html")

def delete_exercises(request: HttpRequest, exercises_id:int):

    try:
        exercises = Exercises.objects.get(id=exercises_id)
    except:
        return render(request)

    exercises.delete()

    return redirect("plan:list_exercises")

def delete_food(request: HttpRequest, food_id:int):

    try:
        food = Food.objects.get(id=food_id)
    except:
        return render(request)

    food.delete()

    return redirect("plan:list_food")