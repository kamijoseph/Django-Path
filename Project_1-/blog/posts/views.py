from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloworld(request):
    return HttpResponse("<h1>Hello World<h1/>")

def post(request, id):
    for post in posts:
        if post['id'] == id:
            post_dict = post
            break
    return HttpResponse(f"{id} ")