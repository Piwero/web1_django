from django.urls import path
# from . import views
from webproject.webapp import views

from . import views
>>>>>>> change import models webapp urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
