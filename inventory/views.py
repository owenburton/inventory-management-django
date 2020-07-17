from django.shortcuts import render, redirect
from .models import *
from .forms import *

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


def add_device(request, deviceClass):
    if request.method == "POST":
        form = deviceClass(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    
    else:
        form = deviceClass()
        return render(request, 'add_new.html', {'form': form})


def add_laptop(request):
    return add_device(request, LaptopForm)

def add_desktop(request):
    return add_device(request, DesktopForm)

def add_mobile(request):
    return add_device(request, MobileForm)