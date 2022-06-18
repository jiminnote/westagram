

from django.db              import models
from validation             import *

class User(models.Model):
    first_name   =models.CharField(max_length=50)
    last_name    =models.CharField(max_length=50)
    nick_name    =models.CharField(max_length=50,unique=True)
    password     =models.CharField(max_length=25)
    email        =models.EmailField(max_length=25,unique=True)
    phone_number =models.CharField(max_length=20)
    
    class Meta:
        db_table='users'