from django.urls import path
from . import views as vs



urlpatterns = [
    path("register", vs.register, name="register"),
    path("login", vs.login, name="login"),
    path("logout", vs.logout, name="logout"),
    
]