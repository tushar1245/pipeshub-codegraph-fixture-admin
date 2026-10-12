const LINKS = ["Dashboard", "Users", "Audit", "Reports"];

export function Sidebar({ active }: { active: string }) {
  return (
    <nav>
      {LINKS.map((l) => (
        <a key={l} className={l === active ? "active" : ""} href={`#${l.toLowerCase()}`}>
          {l}
        </a>
      ))}
    </nav>
  );
}
