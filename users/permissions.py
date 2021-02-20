from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import authentication


class IsAuthReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated

    def has_permission(self, request, view):
        return request.user.is_authenticated


class IsStaffOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff()

    def has_permission(self, request, view):
        return request.user.is_admin()
