from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer


from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
def product_list(request):
    return HttpResponse("This is the product list view.")




@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def test_api(request):
    return Response({"message": "Hello from Django!"})