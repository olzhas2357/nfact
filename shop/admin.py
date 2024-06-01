from django.contrib import admin
from .models import Shop, Cart, CartItem

class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')

admin.site.register(Shop, ShopAdmin)
admin.site.register(Cart)
admin.site.register(CartItem)