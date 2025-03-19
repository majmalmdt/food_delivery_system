from rest_framework import permissions
class IsAdminRole(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and getattr(request.user, 'role', None) == 'admin' 