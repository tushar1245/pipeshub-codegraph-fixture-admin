from app.admin import routes
from app.admin.service import AdminService
from app.shared.audit import AuditLog
from app.shared.db import Database


def create_app(replica_path: str = "/var/lib/acme/replica.db") -> None:
    routes.bind(AdminService(Database(replica_path), AuditLog()))
