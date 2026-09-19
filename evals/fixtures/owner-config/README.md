# Owner Runtime Governance Fixture

Purpose: test safe architecture for owner-controlled appearance settings.

Intentional issues:

- raw persisted values are applied directly
- no draft/published separation
- no schema version
- no validation
- no rollback/audit metadata
- user preferences can override any owner field
- role check is UI-only

The agent should propose or implement a typed validation/resolution boundary without adding arbitrary executable configuration.
