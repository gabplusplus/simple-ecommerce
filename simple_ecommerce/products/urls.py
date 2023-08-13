from django.urls import path
from .views import *

app_name = 'products'

urlpatterns = [
    path('add-product/', ProductCreate.as_view(), name='product_create'),
    path('list/', ProductList.as_view(), name='product_list'),
    path('details/', ProductDetails.as_view(), name='product_details'),
]