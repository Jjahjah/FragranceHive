
from django.urls import path
from .views import test_api
from . import views



urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('api/products/', views.get_products, name='api_products'),
    path("test/", test_api),
]
