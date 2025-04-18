from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    """
    Custom permission to only allow admin users to access certain views.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_admin
    
class IsUserOrAdminPermission(BasePermission):
    """
    Custom permission to allow access to the resource for both admin and regular users.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
