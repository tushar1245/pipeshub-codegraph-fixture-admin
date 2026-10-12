from app.admin.models import StaffUser


class PermissionDenied(Exception):
    pass


def require_permission(user: StaffUser, permission: str) -> None:
    if not user.can(permission):
        raise PermissionDenied(f"{user.email} cannot {permission}")
