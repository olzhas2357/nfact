from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=2000)
    quantity = models.IntegerField()
    image = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class CartItem(models.Model):
    product = models.ForeignKey(Shop, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    
class Cart(models.Model):
    items = models.ManyToManyField(CartItem)
    
    def __str__(self):
        return f"Cart with {self.items.count()} items"