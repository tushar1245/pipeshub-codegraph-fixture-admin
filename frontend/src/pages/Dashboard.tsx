import { formatCount, formatDate } from "../lib/format";

export function DashboardPage({ orders, since }: { orders: number; since: number }) {
  return (
    <section>
      <h1>{formatCount(orders)} orders</h1>
      <small>since {formatDate(since)}</small>
    </section>
  );
}
