from django.urls import path, include
from drfpasswordless.views import ObtainEmailCallbackToken
from rest_framework.routers import DefaultRouter

from .views import ObtainToken, UserViewSet, UserUpdateAPIView

user_router = DefaultRouter()

user_router.register('', UserViewSet, basename='User')

urlpatterns = [
    path('token/', ObtainToken.as_view(), name='obtain_token'),
    path('email/', ObtainEmailCallbackToken.as_view(), name='obtain_email'),
    path('me/', UserUpdateAPIView.as_view(), name='update_user'),
    path('', include(user_router.urls))
]
