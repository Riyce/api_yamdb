from django.contrib import admin
from django.urls import path, include, re_path
from .views import ObtainToken, UserConfigViewSet
from drfpasswordless.views import ObtainEmailCallbackToken
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('token/', ObtainToken.as_view(), name='obtain_token'),
    path('email/', ObtainEmailCallbackToken.as_view(), name='obtain_email'),
    path('me/', csrf_exempt(UserConfigViewSet), name='user_config')
]
