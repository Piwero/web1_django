from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "ProductCategory"
        verbose_name_plural = "ProductCategories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    categories = models.ForeignKey(ProductCategory, on_delete= models.CASCADE)
    image = models.ImageField(upload_to="shop", null=True, blank=True)
    price = models.FloatField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name



