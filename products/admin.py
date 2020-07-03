from django.contrib import admin
from .models import Product, Offer


class OfferInLine(admin.StackedInline):
    model = Offer
    max_num = 1


class ProductAdmin(admin.ModelAdmin):
    # # Manually display fields
    # list_display = ('name', 'price', 'stock')
    # display all fields
    list_display = list(Product().__dict__.keys())[1:]
    # inlines = [OfferInLine]


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'discount')


admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
