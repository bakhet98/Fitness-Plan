from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    username = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True)
    email = models.EmailField()
    first_name = models.TextField()
    last_name = models.TextField()
    password = models.IntegerField()


