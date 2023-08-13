from django.db import models

class Products(models.Model):
    created_at = models.DateTimeField(auto_created=True)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500, null=True)
    product_id = models.CharField(max_length=50)
    price = models.FloatField()
    sale = models.BooleanField(default=False)