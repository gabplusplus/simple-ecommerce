from django.urls import path
from .views import *

app_name = 'checkout'

urlpatterns = [
    path('checkout/', CheckoutCreate.as_view(), name='checkout_create'),
    path('list/', CheckoutList.as_view(), name='checkout_list'),
    path('details/', CheckoutDetails.as_view(), name='checkout_details'),
]