from django.db import models
from cart.models import Cart

# Create your models here.
class Checkout(models.Model):
    item = models.ManyToManyField(Cart, related_name='cart_checkout')
    created_at = models.DateTimeField(auto_created=True)
    address = models.CharField(max_length=255)
    contact = models.EmailField()
