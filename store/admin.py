from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'slug', 'price', 'stock', 'is_available', 'created_at', 'modified_at')
    prepopulated_fields = {'slug': ('product_name',)}

admin.site.register(Product, ProductAdmin)