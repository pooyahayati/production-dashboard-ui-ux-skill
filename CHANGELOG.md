# Changelog

All notable changes to this project are documented here.

## [1.3.0] - 2026-09-20

### Product Design and Runtime Governance

- Added a dedicated Design System Architecture reference for token layering, configuration schemas, precedence, migrations, and maintainable changeability.
- Added Runtime UI Governance with an optional Owner-only UI/UX Control Center.
- Defined safe owner configuration through allowlisted semantic tokens rather than arbitrary CSS, JavaScript, or HTML.
- Added Draft → Preview → Validate → Publish lifecycle, version history, rollback, audit log, reset, import/export, tenant isolation, and failure fallback guidance.
- Added explicit server-side authorization requirements for privileged appearance controls.
- Added deterministic precedence: Locked Constraints → Design System Defaults → Published Owner Config → User Preferences.
- Added user personalization guidance for density, theme, sidebar state, table preferences, saved filters, saved views, and optional dashboard layouts.
- Added role-aware UX and power-user patterns.
- Added Data Trust UX for last-updated time, freshness, source, timezone, active filter scope, stale/partial/sync states, metric definitions, and drill-down traceability.
- Expanded dashboard patterns for saved views, shared-view permissions, role-aware landing experiences, onboarding, and recurring user preferences.
- Expanded existing-product audits to cover maintainability, hard-coded presentation, token architecture, runtime governance, personalization, and data trust.
- Expanded QA to cover configuration authorization, preview/publish/rollback, migrations, cache invalidation, preference precedence, stale data, and runtime fallback.
- Extended Design Profile schema with runtime governance, owner/user/code-only classification, and Data UX fields.
- Added new behavioral evals and public submission coverage for runtime governance and personalization.

## [1.2.0] - 2026-09-20

### Hardening

- Reduced the canonical `SKILL.md` to a route-based entrypoint with progressive disclosure.
- Removed duplicate root Skill/reference copies; `skills/production-dashboard-ui-ux-skill/` is now the single source of truth.
- Rewrote the trigger description to state both when to use and when not to use the Skill.
- Added Collaborative, Delegated, and Audit-only autonomy modes.
- Added explicit working-tree, privacy, production-data, dependency, and asset-license safety.
- Added dedicated performance and accessibility references.
- Added audit coverage reporting and stronger before/after regression criteria.
- Expanded localization beyond RTL/LTR to numbers, currency, dates, timezone, pluralization, text expansion, truncation, and translation-safe strings.
- Added chart accessibility and data-alternative guidance.
- Added Design Profile provenance, status, skill-version, decision-source, and locked-constraint fields.
- Corrected Codex skill-installer URLs to include the required repository path.
- Added validated public Plugin metadata, supported category/capabilities, publisher website/support links, brand colors, logo, and composer icon.
- Shortened Plugin listing fields and starter prompts to public-directory limits.
- Shortened the plugin package name so `plugin-name:skill-name` stays within the public identity limit.
- Reworked submission tests to exactly five positive and three negative cases with expected result format and fixture requirements.
- Added deterministic release packaging, checksums, permanent release workflow, official OpenAI skill validation, and Codex installer smoke testing.
- Added machine-readable behavioral eval cases and forward-testing instructions.

## [1.1.0] - 2026-09-19

### Added

- Dedicated existing-product audit and improvement workflow.
- Observed Baseline for completed/live products without a Design Profile.
- Safe-fix vs strategic-change rules.
- Brand, palette, and logo-treatment audit with controlled refresh support.
- Regression-aware before/after QA.

## [1.0.0] - 2026-09-19

### Added

- Initial public release.
- Design Discovery and Design Profile workflow.
- Dashboard and product UI patterns.
- Persian RTL, English LTR, local fonts, responsive behavior, Light/Dark themes, branding, and visual QA.
- Codex and Claude distribution guidance.
