from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse('hello world') this is for going to the home page directly
    return render(request, "home.html", {"name": "bukunmi"})

def add(request):
    # val1= int(request.GET["num1"]) #this is the old way of accessing val it can raise keyerror if value is not available so .GET.get() is better
    # val2= int(request.GET["num2"])
    # val1= int(request.GET.get("num1")) using .GET.get(), u are sending your data to the address bar which is not save
    # val2= int(request.GET.get("num2"))
    val1= int(request.POST["num1"])    #here post must be with [] and not () cos it not a function
    val2= int(request.POST["num2"])
    ans = val1 + val2
    return render(request, 'result.html', {"result": ans})