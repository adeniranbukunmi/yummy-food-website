from django.urls import path
from . import views as vs

urlpatterns = [
    path("", vs.home, name="home"),
    path("add", vs.add, name="add")
]