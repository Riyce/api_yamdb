from django.contrib.auth import get_user_model
from drfpasswordless.serializers import TokenResponseSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .utils import get_tokens_for_user

from .permissions import IsAuthReadOnly, IsStaffOnly
from .serializers import CallbackTokenAuthSerializer, UserProfileSerializer

User = get_user_model()


class AbstractBaseObtainAuthToken(APIView):
    """
    This is a duplicate of rest_framework's own ObtainAuthToken method.
    Instead, this returns an Auth Token based on our 6 digit callback token and source.
    """
    serializer_class = None

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get('user')
        token = get_tokens_for_user(user)
        token_serializer = TokenResponseSerializer(data=token, partial=True)

        if token_serializer.is_valid():
            return Response(token, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Couldn\'t log you in. Try again later.'}, status=status.HTTP_400_BAD_REQUEST)


class ObtainToken(AbstractBaseObtainAuthToken):
    permission_classes = (AllowAny,)
    serializer_class = CallbackTokenAuthSerializer


class UserUpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthReadOnly,)
    serializer_class = UserProfileSerializer
    lookup_field = 'email'

    def get_object(self):
        user = self.request.user
        return user

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthReadOnly, IsStaffOnly,)
    queryset = User.objects.all()
    lookup_field = 'username'
