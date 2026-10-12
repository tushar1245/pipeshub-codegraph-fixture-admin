export function formatDate(ts: number): string {
  return new Date(ts * 1000).toISOString().slice(0, 10);
}

export const formatCount = (n: number): string => n.toLocaleString("en-US");
