import { activeConfig } from "./config";

export function applyTheme() {
  document.documentElement.style.setProperty("--primary", activeConfig.primary);
  document.documentElement.style.setProperty("--sidebar-width", activeConfig.sidebarWidth + "px");
  if (activeConfig.customCss) {
    const style = document.createElement("style");
    style.textContent = activeConfig.customCss;
    document.head.appendChild(style);
  }
}
