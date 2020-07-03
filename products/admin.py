from django.contrib import admin
from .models import Product, Offer


class ProductInLine(admin.TabularInline):
    model = Product
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    # # Manually display fields
    # list_display = ('name', 'price', 'stock')
    # display all fields
    list_display = list(Product().__dict__.keys())[1:]
    autocomplete_fields = ['offer']


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'discount')
    search_fields = ['description', 'code']
    inlines = [ProductInLine]


admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
