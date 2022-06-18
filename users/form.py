
from django.forms import ModelForm
from django import forms
from .models import *
from validation import *

class UserForm(ModelForm):
    
    
    class Meta:
        model=User
        fields = '__all__'
        

form = UserForm(instance=User.objects.get(pk=1))

