import { DataTable } from "../components/DataTable";
import { useAdminUsers } from "../hooks/useAdminUsers";

export function UsersPage() {
  const users = useAdminUsers();
  return <DataTable rows={users} columns={[{ key: "label", title: "Name" }]} />;
}
