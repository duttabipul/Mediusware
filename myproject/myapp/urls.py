from django.urls import path
from . import views

urlpatterns = [
    path('', views.myfunctioncall, name="index"),
    path('products', views.myfunctionproducts, name="products"),

]