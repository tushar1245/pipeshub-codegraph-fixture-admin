export function ConfirmDialog({ message, onConfirm }: { message: string; onConfirm: () => void }) {
  return (
    <dialog open>
      <p>{message}</p>
      <button onClick={onConfirm}>Confirm</button>
    </dialog>
  );
}
