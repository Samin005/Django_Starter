from django.urls import path, include
from . import views

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = 'http://127.0.0.1:8000/products/accounts/google/login/callback/'
    client_class = OAuth2Client


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
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('dj-rest-auth/google/logout/', views.google_logout, name='google_logout'),
    path('user/', views.login_user, name='user'),
    path('current-user/', views.get_current_user, name='current-user'),
    path('user/logout/', views.logout_user, name='logout'),
    path('set-redirect-url/', views.set_redirect_url, name='set-redirect-url')
]
