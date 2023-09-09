from django.urls import path
from .views import ListView, DetailView , CreateView

urlpatterns = [
    path("", ListView, name="list"),
    path("detail/<int:number>/", DetailView, name="detail"),
    path("create/", CreateView, name="create"),
]