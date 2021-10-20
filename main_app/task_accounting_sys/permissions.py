from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.created_by.id == request.user.id


class IsManagersGroupMemberAndOwnerOrExecutor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if (request.user.groups.filter(name='Managers').exists() and request.user.id == obj.created_by)\
                or request.user.id == obj.executor:
            return True
        return False


class IsManagersGroupMember(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Managers').exists():
            return True
        return False
