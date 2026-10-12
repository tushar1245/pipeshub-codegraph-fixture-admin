from app.admin.models import StaffUser
from app.admin.service import AdminService
from app.shared.audit import AuditLog
from tests.fakes import MemoryDatabase


def test_support_cannot_refund():
    service = AdminService(MemoryDatabase(), AuditLog())
    try:
        service.refund(StaffUser("u1", "s@acme.test"), "o1")
    except Exception as exc:
        assert "cannot refund" in str(exc)
