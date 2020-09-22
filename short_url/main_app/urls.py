from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('shortener/<int:pk>/', views.reroute, name="reroute")
]