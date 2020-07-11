from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from Django_Starter import views, settings
from .models import Product, Offer
from .apps import ProductsConfig
from .serializers import ProductSerializer, OfferSerializer, UserSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response


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


class UserAPIAll(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['POST'])
def set_redirect_url(request):
    views.redirect_url = request.data['current_url'] + '/'
    return Response({"success": True, 'redirect_url': views.redirect_url})


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


def index(request):
    views.redirect_url = settings.root_url + ProductsConfig.name + '/'
    return render(request, 'products/index.html', {'products': Product.objects.all()})


def new(request):
    return HttpResponse('New Product')
