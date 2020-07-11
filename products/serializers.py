from django.contrib.auth.models import User

from .models import Product, Offer
from rest_framework import serializers


class ProductSerializerModelOnly(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OfferSerializerModelOnly(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    offer = OfferSerializerModelOnly(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class OfferSerializer(serializers.HyperlinkedModelSerializer):
    products = ProductSerializerModelOnly(many=True, read_only=True)

    class Meta:
        model = Offer
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'is_anonymous', 'is_authenticated']
