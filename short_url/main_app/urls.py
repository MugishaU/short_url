from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('short/<int:pk>/', views.reroute, name="reroute"),
    path('newurl/<int:pk>', views.newurl, name="newurl")
]