from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    return render(request, 'webapp/home.html')


def services(request):
    return render(request, 'webapp/services.html')


def shop(request):
    return render(request, 'webapp/shop.html')


def blog(request):
    return render(request, 'webapp/blog.html')


def contact(request):
    return render(request, 'webapp/contact')

