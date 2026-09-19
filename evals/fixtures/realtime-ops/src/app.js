let incidents = [];
let selectedId = null;

export function onIncoming(next) {
  incidents = next.sort((a, b) => b.severity - a.severity);
  selectedId = null;
  render();
}

export async function acknowledge(id) {
  await fetch("/api/incidents/" + id + "/ack", { method: "POST" });
}

export function setConnection(connected) {
  document.body.dataset.connected = String(connected);
}

function render() {
  // Fixture intentionally omits stable-selection and incremental update behavior.
}
