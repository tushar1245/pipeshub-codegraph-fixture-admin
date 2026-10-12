from app.admin.models import StaffUser
from app.admin.service import AdminService

_service: AdminService | None = None


def bind(service: AdminService) -> None:
    global _service
    _service = service


def refund_order(user: StaffUser, order_id: str) -> dict:
    return {"refunded": _service.refund(user, order_id)}


def dashboard() -> dict:
    return {"orders": _service.order_count()}
