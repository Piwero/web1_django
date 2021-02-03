from django.urls import path
from webapp import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('services/', views.services, name='Services'),
    path('shop/', views.shop, name='Shop'),
    path('blog/', views.blog, name='Blog'),
    path('contact/', views.contact, name='Contact'),

]