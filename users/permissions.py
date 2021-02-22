from rest_framework import permissions


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
