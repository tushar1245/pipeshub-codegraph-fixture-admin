from dataclasses import dataclass, field
import time


@dataclass
class AuditEntry:
    actor: str
    action: str
    target: str
    at: float = field(default_factory=time.time)


class AuditLog:
    def __init__(self) -> None:
        self.entries: list[AuditEntry] = []

    def record(self, actor: str, action: str, target: str) -> AuditEntry:
        entry = AuditEntry(actor, action, target)
        self.entries.append(entry)
        return entry

    def by_actor(self, actor: str) -> list[AuditEntry]:
        return [e for e in self.entries if e.actor == actor]
