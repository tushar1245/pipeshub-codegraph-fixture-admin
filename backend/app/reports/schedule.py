from app.reports.exports import export_refunds
from app.shared.db import Database
from app.shared.retry import retry_with_backoff


def nightly(db: Database) -> str:
    return retry_with_backoff(lambda: export_refunds(db))
