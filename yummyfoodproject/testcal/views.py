from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse('hello world') this is for going to the home page directly
    return render(request, "home.html", {"name": "bukunmi"})