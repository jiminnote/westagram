from django.urls import path
from .views import *

urlpatterns = [
    path('/post',PostView.as_view())
]

