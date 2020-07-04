from django.db import models


class Product(models.Model):
    name = models.CharField(unique=True, max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    offer = models.ForeignKey('Offer', on_delete=models.CASCADE, default=1, related_name='products')

    def __str__(self):
        return self.name


class Offer(models.Model):
    code = models.CharField(unique=True, max_length=7)
    description = models.CharField(max_length=255)
    discount = models.FloatField(default=0.0)

    def __str__(self):
        return self.code + ' - ' + self.description
