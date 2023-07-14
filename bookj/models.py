from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    firstname = models.CharField(max_length=100,null=True)
    lastname = models.CharField(max_length=100,null=True)



class Book(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    author = models.CharField(max_length=50)