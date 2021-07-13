from django.db import models

from django.db import *

# Create your models here.
class Service(models.Model):
    title = \
        models.CharField(max_length=50 )
    content = models.\
        CharField(max_length=50)
    image = models.ImageField( upload_to="services")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "service"
        verbose_name_plural = "services"

    def __str__(self):
        return self.title
