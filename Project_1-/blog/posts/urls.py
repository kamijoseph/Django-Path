
from django.urls import path
from . import views

urlpatterns = [
    path('helloworld/', views.helloworld),
    path("<id>/", views.post)
]