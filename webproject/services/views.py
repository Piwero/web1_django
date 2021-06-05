from django.shortcuts import render
from services.models import Service


# Create your views here.
def services(request):
    services = Service.objects.all()

    return render(request, "services/services.html", {"services": services})
