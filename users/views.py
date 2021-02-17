from drfpasswordless.views import AbstractBaseObtainAuthToken
from rest_framework.permissions import AllowAny

from .serializers import CallbackTokenAuthSerializer


class ObtainToken(AbstractBaseObtainAuthToken):
    permission_classes = (AllowAny,)
    serializer_class = CallbackTokenAuthSerializer

