from django.shortcuts import render
from django.http import HttpResponse
from .models import FoodCatalogue

# Create your views here.

def index(request):
    fooditem1=FoodCatalogue()
    fooditem1.name = "amaladudu"
    fooditem1.price = 14
    fooditem1.img='amalaatiewedu.jpg'
    fooditem1.description="balance meal for good growth"
    # fooditem1.offer=True

    fooditem2=FoodCatalogue()
    fooditem2.name = "tomato and hot dog"
    fooditem2.price = 5
    fooditem2.img="salad2.jpg"
    fooditem2.description="hot dogs for the light"
    # fooditem2.offer=False


    fooditem3=FoodCatalogue()
    fooditem3.name = "onions and beans"
    fooditem3.price = 10
    fooditem3.img="jollof-rice2-1.webp"
    fooditem3.description="proteinous food"
    # fooditem3.offer=False


    all_food=[fooditem1,fooditem2,fooditem3]

    # return HttpResponse('hello world') this is for going to the home page directly
    return render(request, "index.html", {"fooditems":all_food})
