from dataclasses import dataclass


@dataclass
class StaffUser:
    id: str
    email: str
    role: str = "support"

    def can(self, permission: str) -> bool:
        return permission in ROLE_PERMISSIONS.get(self.role, ())


ROLE_PERMISSIONS = {
    "support": ("read",),
    "admin": ("read", "refund", "suspend"),
}
