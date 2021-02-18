from drfpasswordless.views import AbstractBaseObtainAuthToken
from rest_framework.permissions import AllowAny
from rest_framework import viewsets

from .serializers import CallbackTokenAuthSerializer, UserProfileSerializer


class ObtainToken(AbstractBaseObtainAuthToken):
    permission_classes = (AllowAny,)
    serializer_class = CallbackTokenAuthSerializer


class UserConfigViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
