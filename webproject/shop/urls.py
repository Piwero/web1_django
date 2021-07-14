from django.urls import path

from .views import shop

urlpatterns = [
    path("", shop, name="shop"),
]
