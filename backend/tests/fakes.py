from app.shared.db import Database


class MemoryDatabase(Database):
    def __init__(self) -> None:
        super().__init__(":memory:")
