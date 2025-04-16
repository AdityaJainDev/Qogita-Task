from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=50, unique=True)
    barcode = models.CharField(max_length=50)
    inventory_quantity = models.IntegerField()
    size = models.IntegerField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title
