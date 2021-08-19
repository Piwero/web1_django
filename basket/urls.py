from django.urls import path

from . import views

app_name = "basket"
urlpatterns = [
    path("add/<int:product_id>/", views.add_product, name="add"),
    path("reduce/<int:product_id>/", views.reduce_product, name="reduce"),
    path("eliminate/<int:product_id>/", views.eliminate_product, name="eliminate"),
    path("reset/", views.reset_basket, name="reset"),
]
