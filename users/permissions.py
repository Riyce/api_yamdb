from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import authentication


class IsAuthReadOnly(permissions.BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """
    def has_object_permission(self, request, view, obj):
        #return True
        return obj.author == request.user

    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS
            or request.user
            and request.user.is_authenticated
        )

