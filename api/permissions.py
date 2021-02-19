from rest_framework import permissions


#class IsAdminOrReadOnly(permissions.BasePermission):
    #def has_object_permission(self, request, view, obj):
        #if request.method != 'GET':
            #return request.user.profile__role == 'Admin'
        #return True
