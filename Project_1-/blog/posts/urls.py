
from django.urls import path
from . import urls

urlpatterns = [
    path('posts/helloworld/', views.helloworld)
]
