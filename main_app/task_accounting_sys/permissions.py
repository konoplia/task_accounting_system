from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.created_by.id == request.user.id


class IsManagersGroupMemberOrExecutor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name='Managers').exists() or request.user.id == obj.executor:
            return True
        return False
