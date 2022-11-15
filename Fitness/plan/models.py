from django.db import models

# Create your models here.


class Exercises(models.Model):

    name_exercises = models.TextField()
    day_exercises = models.TextField()
    counts_exercises = models.IntegerField()
    sets_exercises = models.IntegerField()
    weight_exercises = models.FloatField()

class Food(models.Model):

    meal = models.TextField()
    colres = models.FloatField()
    


    
