from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsUser(permissions.BasePermission):
    """Проверка прав пользователя"""

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return request.user == view.get_object()


class IsOwner(BasePermission):
    """Проверка прав доступа для владельца"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
