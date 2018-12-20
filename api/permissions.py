from rest_framework.permissions import BasePermission
from items.models import Item


class IsAddedBy(BasePermission):
    message = "You must be the user who added this items."

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or (obj.added_by == request.user):
            return True
        else:
            return False