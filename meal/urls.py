from django.urls import path
from . import views

urlpatterns = [
    path("showItem/", views.index, name="showItem"),
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
]