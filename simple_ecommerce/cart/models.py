from django.db import models
from products.models import Products

class Cart(models.Model):
    item = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='cart_item')
    quantity = models.FloatField()
    total_price = models.FloatField()
    checked_out = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.total_price = self.item.price * self.quantity
        super(Cart, self).save(*args, **kwargs)