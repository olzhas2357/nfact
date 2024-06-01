from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=2000)
    quantity = models.IntegerField()
    image = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
