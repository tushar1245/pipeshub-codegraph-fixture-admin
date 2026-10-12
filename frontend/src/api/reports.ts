import { getJson, postJson } from "../lib/http";

export interface Report {
  id: string;
  label: string;
}

export function listReports(): Promise<Report[]> {
  return getJson<Report[]>("/reports");
}

export function createReports(input: Omit<Report, "id">): Promise<Report> {
  return postJson<Report>("/reports", input);
}
