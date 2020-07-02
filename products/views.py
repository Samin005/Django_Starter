from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Offer

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .serializers import ProductSerializer, OfferSerializer


class ProductsAPIAll(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

    def update(self, request, *args, **kwargs):
        product_creator_user_id = 1
        if request.user.id != product_creator_user_id:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data={
                'detail': f'You are not allowed to update product {self.get_object().name}({self.get_object().id})'
            })
        else:
            return super(ProductsAPIAll, self).update(request)


class OffersAPIAll(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


def index(request):
    return render(request, 'products/index.html', {'products': Product.objects.all()})


def new(request):
    return HttpResponse('New Product')
