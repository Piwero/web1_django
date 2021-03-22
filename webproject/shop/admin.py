from django.contrib import admin
from .models import ProductCategory, Product


class ProductCategoryAdmin(admin.ModelAdmin):

    readonly_fields = ('created', "updated")


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created', "updated")


admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)


