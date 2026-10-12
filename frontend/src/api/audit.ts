import { getJson, postJson } from "../lib/http";

export interface AuditEntry {
  id: string;
  label: string;
}

export function listAudit(): Promise<AuditEntry[]> {
  return getJson<AuditEntry[]>("/audit");
}

export function createAudit(input: Omit<AuditEntry, "id">): Promise<AuditEntry> {
  return postJson<AuditEntry>("/audit", input);
}
