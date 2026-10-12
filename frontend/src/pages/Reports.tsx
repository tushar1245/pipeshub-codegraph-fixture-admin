import { createReports } from "../api/reports";
import { ConfirmDialog } from "../components/ConfirmDialog";

export function ReportsPage() {
  const run = () => createReports({ label: "refunds" });
  return <ConfirmDialog message="Generate the refunds report?" onConfirm={run} />;
}
