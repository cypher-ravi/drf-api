from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    custom permission to only allow owners of an object to edit it

    """

    def has_object_permission(self, request, view ,obj):
        #Read permissions are allwed to any request
        #so we'll always allow GET ,HEAD or options request.
        if request.method in permissions.SAFE_METHODS:
            return True

        #write permissions are only allowed to owner of the snippet
        return  obj.owner == request.user