from app.admin.models import StaffUser
from app.admin.policies import require_permission
from app.shared.audit import AuditLog
from app.shared.db import Database
from app.shared.retry import retry_with_backoff


class AdminService:
    def __init__(self, db: Database, audit: AuditLog) -> None:
        self.db = db
        self.audit = audit

    def refund(self, user: StaffUser, order_id: str) -> bool:
        require_permission(user, "refund")
        self.audit.record(user.id, "refund", order_id)
        return retry_with_backoff(lambda: self._mark_refunded(order_id))

    def suspend(self, user: StaffUser, customer_id: str) -> None:
        require_permission(user, "suspend")
        self.audit.record(user.id, "suspend", customer_id)

    def order_count(self) -> int:
        return self.db.scalar("select count(*) from orders") or 0

    def _mark_refunded(self, order_id: str) -> bool:
        return bool(self.db.query("select 1 from orders where id = ?", order_id))
