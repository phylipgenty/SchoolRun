from functools import wraps

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission


def role_required(*roles):
    """Restrict a Django view to logged-in users with one of the given roles."""

    def decorator(view):
        @wraps(view)
        @login_required
        def wrapper(request, *args, **kwargs):
            if request.user.role not in roles:
                raise PermissionDenied
            return view(request, *args, **kwargs)

        return wrapper

    return decorator


class HasRole(BasePermission):
    """DRF permission: subclass and set `roles`."""

    roles = ()

    def has_permission(self, request, view):
        user = request.user
        return bool(user and user.is_authenticated and user.role in self.roles)


class IsSchoolAdmin(HasRole):
    roles = ("school_admin",)


class IsParent(HasRole):
    roles = ("parent",)


class IsDriver(HasRole):
    roles = ("driver",)


class IsMarshal(HasRole):
    roles = ("marshal",)
