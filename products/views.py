from django.shortcuts import render
from . models import Products
def showproducts(request):
    products = Products.objects.all()
    context ={'products':products}
    return render(request,'products.html',context)
def index(request):
    return render(request,'index.html')


# Create your views here.
