from drfpasswordless.views import AbstractBaseObtainAuthToken
from drfpasswordless.serializers import TokenResponseSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.authentication import get_authorization_header
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView, )
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from .permissions import IsAuthenticatedOrReadOnly

from .serializers import CallbackTokenAuthSerializer, UserProfileSerializer

from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class AbstractBaseObtainAuthToken(APIView):
    """
    This is a duplicate of rest_framework's own ObtainAuthToken method.
    Instead, this returns an Auth Token based on our 6 digit callback token and source.
    """
    serializer_class = None

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            token = get_tokens_for_user(user)
            token_serializer = TokenResponseSerializer(data=token, partial=True)

            if token_serializer.is_valid():
                return Response(token, status=status.HTTP_200_OK)
        # else:
        #    logger.error("Couldn't log in unknown user. Errors on serializer: {}".format(serializer.error_messages))
        # return Response({'detail': 'Couldn\'t log you in. Try again later.'}, status=status.HTTP_400_BAD_REQUEST)


class ObtainToken(AbstractBaseObtainAuthToken):
    permission_classes = (AllowAny,)
    serializer_class = CallbackTokenAuthSerializer


class UserUpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserProfileSerializer
    lookup_field = 'email'

    def get_object(self):
        email = self.request.data.get('email')
        return get_object_or_404(User, email=email)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    lookup_field = 'username'

    def get_queryset(self):
        out = User.objects.all()
        print(out)
        return out



class UserConfigViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()
