# Real-time Operations Fixture

Purpose: test real-time stability, connection/freshness UX, duplicate actions, and incoming-update behavior.

Intentional issues:

- rows are fully re-sorted every update
- selection is lost
- no disconnected/stale state
- repeated acknowledge clicks can execute twice
- no pause/freeze behavior
