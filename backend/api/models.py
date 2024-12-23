from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)  # Product name
    description = models.TextField(blank=True, null=True)  # Product description
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Product price
    stock = models.IntegerField()  # Stock quantity
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the product was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for last update

    def __str__(self):
        return self.name
