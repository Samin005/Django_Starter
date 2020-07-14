from django.urls import path, include
from . import views

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register('products', views.ProductsAPIAll)
router.register('offers', views.OffersAPIAll)
router.register('user', views.UserAPIAll)

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth-token/', obtain_auth_token, name='auth-token'),
    path('accounts/', include('allauth.urls')),
    path('jwt-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt-token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', views.login_user, name='user'),
    path('user/logout/', views.logout_user, name='logout'),
    path('set-redirect-url/', views.set_redirect_url, name='set-redirect-url')
]
