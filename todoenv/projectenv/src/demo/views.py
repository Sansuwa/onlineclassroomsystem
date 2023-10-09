from django.shortcuts import render
from demo.models import Product
# from django.http import HttpResponse


# Create your views here.

def home(request):
    # print(request)
    # return HttpResponse("<h1> Response accepted <h1>")
    products = Product.objects.all()
    data = {"products":products}
    # data = {"name":"Shyam","address":"Kathmandu,"}
    return render(request, "home.html",data)
