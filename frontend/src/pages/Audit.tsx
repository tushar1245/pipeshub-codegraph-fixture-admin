import { useEffect, useState } from "react";
import { listAudit, type AuditEntry } from "../api/audit";
import { DataTable } from "../components/DataTable";

export function AuditPage() {
  const [entries, setEntries] = useState<AuditEntry[]>([]);
  useEffect(() => {
    listAudit().then(setEntries);
  }, []);
  return <DataTable rows={entries} columns={[{ key: "label", title: "Action" }]} />;
}
