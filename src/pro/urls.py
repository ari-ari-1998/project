from django.urls import path
from .views import ListView, DetailView , CreateView, UpdateFormView, DeleteView

urlpatterns = [
    path("", ListView, name="list"),
    path("detail/<int:pk>/", DetailView, name="detail"),
    path("create/", CreateView, name="create"),
    path("update/<int:pk>/", UpdateFormView, name="update"),
    path("delete/<int:pk>/", DeleteView, name="delete"),
]