from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here.

class CustomUser(AbstractBaseUser):
    account_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=1000, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()


class Wishlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # product = models.ForeignKey
