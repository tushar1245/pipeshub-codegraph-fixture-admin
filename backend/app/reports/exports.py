import csv
import io

from app.shared.db import Database


def export_refunds(db: Database) -> str:
    out = io.StringIO()
    writer = csv.writer(out)
    for row in db.query("select id, amount from refunds"):
        writer.writerow(row)
    return out.getvalue()
