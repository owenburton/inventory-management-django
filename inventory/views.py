from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')


def display_laptops(request):
    items = Laptop.objects.all()
    context = {
        'items': items,
        'header': 'Laptops'
    }

    return render(request, 'index.html', context)


def display_desktops(request):
    items = Desktop.objects.all()
    context = {
        'items': items,
        'header': 'Desktops'
    }

    return render(request, 'index.html', context)


def display_mobiles(request):
    items = Mobile.objects.all()
    context = {
        'items': items,
        'header': 'Mobiles'
    }

    return render(request, 'index.html', context)