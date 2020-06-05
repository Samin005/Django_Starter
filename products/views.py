from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def index(request):
    return render(request, 'products/index.html', {'products': Product.objects.all()})


def new(request):
    return HttpResponse('New Product')
