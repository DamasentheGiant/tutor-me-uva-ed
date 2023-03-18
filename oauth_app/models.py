from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_tutor = models.BooleanField(default=False)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.TextField(max_length=200)
    year = models.TextField(max_length = 500)
    classes = models.TextField(max_length = 1000, default= "")
#   verify_student = models.BooleanField(default=False)
#   verify_tutor = models.BooleanField(default=False)

class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.TextField(max_length=200)
    year = models.TextField(max_length = 500)
    classes = models.TextField(max_length = 1000, default= "")
#   verify_student = models.BooleanField(default=False)
#   verify_tutor = models.BooleanField(default=False)

