import { getJson, postJson } from "../lib/http";

export interface StaffUser {
  id: string;
  label: string;
}

export function listUsers(): Promise<StaffUser[]> {
  return getJson<StaffUser[]>("/staff");
}

export function createUsers(input: Omit<StaffUser, "id">): Promise<StaffUser> {
  return postJson<StaffUser>("/staff", input);
}
