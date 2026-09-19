import { activeConfig } from "./config";

export function OwnerSettings({ user }: { user: { role: string } }) {
  if (user.role !== "owner") return null; // fixture: UI-only role check
  return (
    <form>
      <label>Primary <input defaultValue={activeConfig.primary} /></label>
      <label>Density <input defaultValue={activeConfig.density} /></label>
      <label>Custom CSS <textarea defaultValue={activeConfig.customCss} /></label>
      <button>Save live</button>
    </form>
  );
}
