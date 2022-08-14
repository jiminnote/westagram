import json

from django.shortcuts import render
from django.http      import JsonResponse
from django.views     import View
from .models          import Post
from core.utils       import Signin_decorator 

# Create your views here.
class PostView(View):
    @Signin_decorator 
    def post(self,request):
        try:
            data = json.loads(request.body)
            Post.objects.create(
                user      = request.user,
                img_urls  = data['img_urls'],
                posts     = data['posts']
         )
        
            return JsonResponse({"messge":"SUCCESS"},status=201)
        except:
            return JsonResponse({"messgae":"KEY_ERROR"},status=401)
        