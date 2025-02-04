from django.urls import path
from .views import homeView, successView



urlpatterns = [
    path("", homeView, name="home"),#urlni viewga bo'lab nom beramiz
    path("success/", successView, name="success"),
]
