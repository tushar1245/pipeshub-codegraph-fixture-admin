import { useEffect, useState } from "react";
import { listUsers, type StaffUser } from "../api/users";

export function useAdminUsers(): StaffUser[] {
  const [users, setUsers] = useState<StaffUser[]>([]);
  useEffect(() => {
    listUsers().then(setUsers);
  }, []);
  return users;
}
