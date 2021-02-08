from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):

    return render(request, 'webapp/home.html')


def shop(request):

    return render(request, 'webapp/shop.html')

