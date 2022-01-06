from rest_framework import permissions


class IsAuthenticatedOrCreate(permissions.IsAuthenticated):

    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return super(IsAuthenticatedOrCreate, self).has_permission(request, view)


class IsOwnerOrReadOnly(permissions.IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class IsOwner(permissions.IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
