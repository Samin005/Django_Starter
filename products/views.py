from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from Django_Starter import views, settings
from .models import Product, Offer
from .apps import ProductsConfig
from .serializers import ProductSerializer, OfferSerializer, UserSerializer

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import viewsets, permissions, status
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.response import Response

from rest_framework_simplejwt.authentication import JWTAuthentication


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
    authentication_classes = [JWTAuthentication]


@api_view(['POST'])
def set_redirect_url(request):
    views.redirect_url = request.data['current_url'] + '/'
    return Response({"success": True, 'redirect_url': views.redirect_url})


@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([TokenAuthentication, BasicAuthentication])
def get_current_user(request):
    # Auth-token
    if request.method == 'GET':
        if request.user.is_authenticated:
            login(request, request.user, backend='rest_framework.authentication.TokenAuthentication')
            print(request.user.username + ' logged in')
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    # Basic Auth
    elif request.method == 'POST':
        user: User = authenticate(username=request.data['username'], password=request.data['password'])
        if user is not None:
            login(request, user)
            print(user.username + ' logged in')
        serializer = UserSerializer(user)
        return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def login_user(request):
    if request.user.is_authenticated:
        login(request, request.user, backend='rest_framework_simplejwt.authentication.JWTAuthentication')
        print(request.user.username + ' has logged in')
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([JWTAuthentication, TokenAuthentication, BasicAuthentication])
def logout_user(request):
    # if request.user.is_authenticated:
    #     request.user.auth_token.delete()
    #     print('token deleted')
    logout(request)
    print('logged out')
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


def index(request):
    views.redirect_url = settings.root_url + ProductsConfig.name + '/'
    return render(request, 'products/index.html', {'products': Product.objects.all()})


def new(request):
    return HttpResponse('New Product')
