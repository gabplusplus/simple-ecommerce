from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    path('addtocart/', CartCreate.as_view(), name='cart_add'),
    path('list/', CartList.as_view(), name='cart_list'),
    path('details/', CartDetails.as_view(), name='cart_details'),
]