from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path("", views.blog, name="blog"),
    path("category/<int:category_id>/", views.category, name="category"),
]
