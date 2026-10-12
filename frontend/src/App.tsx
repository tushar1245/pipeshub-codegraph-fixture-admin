import { useState } from "react";
import { Sidebar } from "./components/Sidebar";
import { AuditPage } from "./pages/Audit";
import { DashboardPage } from "./pages/Dashboard";
import { ReportsPage } from "./pages/Reports";
import { UsersPage } from "./pages/Users";

export default function App() {
  const [page, setPage] = useState("Dashboard");
  return (
    <div onClick={() => setPage(page)}>
      <Sidebar active={page} />
      {page === "Users" && <UsersPage />}
      {page === "Audit" && <AuditPage />}
      {page === "Reports" && <ReportsPage />}
      {page === "Dashboard" && <DashboardPage orders={0} since={0} />}
    </div>
  );
}
