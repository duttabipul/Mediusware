from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def myfunctioncall(request):
    return HttpResponse("Hello World")

def myfunctionproducts(request):
    return render(request, "products.html")