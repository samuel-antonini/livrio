from django.urls import path, include
from . import views


urlpatterns = [
    path('loader/', views.loader, name="loader"),
]
