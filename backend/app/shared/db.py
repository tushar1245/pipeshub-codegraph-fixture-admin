"""Read-only replica access for the admin console."""
import sqlite3


class Database:
    def __init__(self, path: str) -> None:
        self.conn = sqlite3.connect(path)

    def query(self, sql: str, *params) -> list[tuple]:
        return self.conn.execute(sql, params).fetchall()

    def scalar(self, sql: str, *params):
        rows = self.query(sql, *params)
        return rows[0][0] if rows else None
