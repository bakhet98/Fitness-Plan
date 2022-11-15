from django.urls import path
from . import views

app_name = "plan"

urlpatterns = [
    path("home/", views.home, name="home"),
    path("exercises/", views.exercises, name="exercises"),
    path("profile/", views.list_exercises, name="list_exercises")
    
]