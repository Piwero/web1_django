from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    return HttpResponse('Home')


def services(request):
    return HttpResponse('Services')


def shop(request):
    return HttpResponse('Shop')


def blog(request):
    return HttpResponse('Blog')


def contact(request):
    return HttpResponse('Contact')

