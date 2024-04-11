from django.shortcuts import render
from django.http import HttpResponse
from .models import FoodCatalogue

# Create your views here.

def index(request):
 
    all_food=FoodCatalogue.objects.all()

    # return HttpResponse('hello world') this is for going to the home page directly
    return render(request, "index.html", {"fooditems":all_food})
