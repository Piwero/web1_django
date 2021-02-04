from django.shortcuts import render, HttpResponse

from services.models import Service


# Create your views here.
def home(request):

    return render(request, 'webapp/home.html')


def services(request):
    services = Service.objects.all()

    return render(request, 'webapp/services.html', {"services": services})


def shop(request):

    return render(request, 'webapp/shop.html')


def blog(request):

    return render(request, 'webapp/blog.html')


def contact(request):
    return render(request, 'webapp/contact.html')

