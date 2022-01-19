from products.models import Product
from django.contrib import admin

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug": ("name",)}

admin.site.register(Product,ProductAdmin)