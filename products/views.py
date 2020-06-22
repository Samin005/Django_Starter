from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Offer

from rest_framework import viewsets
from .serializers import ProductSerializer, OfferSerializer


class ProductsAPIAll(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer


class OffersAPIAll(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


def index(request):
    return render(request, 'products/index.html', {'products': Product.objects.all()})


def new(request):
    return HttpResponse('New Product')
