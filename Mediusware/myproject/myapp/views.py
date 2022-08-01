from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def myfunctioncall(request):
    return HttpResponse("Mediusware Ltd. Type 'products' after the localhost. Such as : http://127.0.0.1:8000/products")

def myfunctionproducts(request):
    return render(request, "products.html")