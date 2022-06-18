
from django.db              import models
from validation             import *
from django.forms import ModelForm

class User(models.Model):
    first_name   =models.CharField(max_length=50,validators=[validate_name],default=None, null=True)
    last_name    =models.CharField(max_length=50,validators=[validate_name],default=None, null=True)
    nick_name    =models.CharField(max_length=50,unique=True,default=None, null=True)
    password     =models.CharField(max_length=500,validators=[validate_password],default=None, null=True)
    email        =models.EmailField(max_length=25,validators=[validate_email],unique=True,default=None, null=True)
    phone_number =models.CharField(max_length=20,validators=[validate_phone_number],default=None, null=True)
    
    class Meta:
        db_table='users'