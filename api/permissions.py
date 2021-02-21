from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        if request.user.is_authenticated:
            return request.user.is_admin()


class IsAuthorOrAdminOrModeratorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method != 'POST':
            return request.user.is_staff() or obj.author == request.user
