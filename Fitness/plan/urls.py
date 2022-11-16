from django.urls import path
from . import views

app_name = "plan"

urlpatterns = [
    path("home/", views.home, name="home"),
    path("exercises/", views.exercises, name="exercises"),
    path("meals/", views.meal, name="meal"),
    path("profile/", views.list_exercises, name="list_exercises"),
    path("plans/", views.plansAvailable, name="plansAvailable"),
    path("plan/delete/<exercises_id>/",views.delete_exercises,name="delete_exercises"),
    path("plan/delete/<food_id>/",views.delete_food,name="delete_food")
    
    
]