from django.urls import path, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('products', views.ProductsAPIAll)
router.register('offers', views.OffersAPIAll)

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('accounts/', include('allauth.urls'))
]
