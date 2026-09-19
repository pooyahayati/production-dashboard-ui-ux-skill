---
name: production-dashboard-ui-ux-skill
description: Design, audit, improve, and redesign production dashboards, admin panels, CRM, analytics, and operational product UI. Use for dashboard UI/UX, existing-product reviews, responsive or RTL/LTR work, themes, branding, tables, forms, navigation, accessibility, performance, or visual QA. Do not use for backend-only work, marketing sites, or unrelated graphic design.
---

# Production Dashboard UI/UX Skill

Build and improve production interfaces for real work, not screenshot-first demos.

Core principle:

> Design for the task, not for the screenshot.

## Route the task first

Choose the smallest mode that fits the request.

### New product

Use when there is no established interface.

Read:
- `references/discovery-and-profile.md`
- the relevant domain references
- `references/qa-checklist.md` before completion

Typical flow:

`Inspect -> Discover -> Recommend -> Approve or Delegate -> Foundation -> Representative Screen -> Roll Out -> QA`

### Existing product — audit only

Use when the user asks to review, critique, assess, or report problems.

Read:
- `references/existing-product-audit.md`
- `references/qa-checklist.md`

Do not modify code or assets unless requested.

### Existing product — audit and improve

Use when the user asks to fix, modernize, improve, polish, or redesign an existing product.

Read:
- `references/existing-product-audit.md`
- `references/execution-safety.md`
- relevant visual/domain references
- `references/qa-checklist.md`

Typical flow:

`Baseline -> Audit -> Prioritize -> Fix -> Validate -> Compare -> Refine`

If no approved `design-profile.md` exists, infer an Observed Baseline first. Do not force a full discovery interview for local corrective work.

### Targeted UI change

Use when the request is narrow, such as a table, form, palette, mobile issue, RTL defect, theme issue, typography problem, or logo treatment.

Inspect the affected surface and read only the relevant references.

Do not expand the assignment unnecessarily.

## Autonomy and approvals

Respect the user's working style.

### Collaborative mode

Use when the user wants to review major design decisions.

Pause before broad changes to:
- primary navigation
- information architecture
- core workflows
- global palette or typography
- design-system foundation
- actual logo artwork or brand identity
- UI framework or component-library migration

### Delegated mode

Use when the user explicitly asks the agent to make reasonable design decisions and complete the work without repeated approvals.

Proceed within the requested scope, but still do not silently:
- weaken permissions or security
- change business rules or data meaning
- remove product capabilities
- replace the actual brand identity unless that was requested
- introduce a major framework migration without a clear need

Document significant decisions at the end.

### Audit-only mode

Never modify code, configuration, or assets.

## Non-negotiable invariants

1. Inspect before changing.
2. Preserve user intent and scope.
3. Preserve business logic, permissions, validation, routing, API contracts, and data semantics unless explicitly authorized.
4. Treat working-tree safety and user-authored changes as protected; read `references/execution-safety.md` for implementation work.
5. Reuse the existing stack before adding dependencies.
6. Existing visual design is not sacred. Improve weak hierarchy, palette, typography, component styling, brand treatment, and responsive behavior when justified.
7. Treat Persian RTL and English LTR as native modes, not post-processing.
8. Treat responsive behavior as product architecture, not a final CSS patch.
9. Use supplied/local fonts and brand assets responsibly; check licensing before adding third-party assets.
10. Do not call a major UI task complete without QA of the rendered result when rendering/browser access is available.
11. Report what was actually inspected and what was not.
12. Do not claim improvement merely because the interface looks newer.

## Reference routing

Read references only when relevant.

- `references/discovery-and-profile.md` — discovery, design-profile lifecycle, partial rediscovery, provenance
- `references/existing-product-audit.md` — existing-product baseline, audit matrix, severity, safe vs strategic fixes
- `references/execution-safety.md` — git/working-tree safety, data/privacy boundaries, scoped implementation
- `references/design-presets.md` — style vocabulary and visual-direction options
- `references/dashboard-patterns.md` — dashboard, navigation, table, form, filter, chart, state, auth, system-page patterns
- `references/rtl-ltr-typography.md` — RTL/LTR, bilingual UI, localization, fonts, mixed-direction content
- `references/theme-responsive-brand.md` — theme, responsive behavior, palette, logo/brand, icons, motion
- `references/accessibility.md` — WCAG-oriented implementation and verification
- `references/performance.md` — frontend performance and perceived-performance review
- `references/qa-checklist.md` — final validation and coverage reporting

## Existing product baseline

Before broad changes, determine enough of the current product to understand:
- shell and navigation
- high-frequency workflows
- representative pages
- components and tokens
- typography and palette
- themes
- responsive behavior
- RTL/LTR/localization
- auth and permission-sensitive surfaces
- loading, empty, error, partial, disabled, and success states
- tests and available visual/browser tooling

For large products, sample representative surfaces first. Record audit coverage rather than implying the whole application was inspected.

## Design profile

For new products or strategic redesigns, create or update `design-profile.md` using `references/discovery-and-profile.md`.

For existing products:
- keep an approved profile authoritative unless the user approves a revision
- use an Observed Baseline for corrective work when no profile exists
- use Partial Rediscovery when only selected strategic fields need to change

## Product-first decisions

Before designing a screen, establish:
- who uses it
- why they open it
- what they must know
- what they must do
- what happens next

Prefer hierarchy, typography, spacing, grouping, and alignment before adding containers.

Do not default to:
- four KPI cards
- nested cards
- excessive pills
- excessive radius or shadow
- decorative gradients or glass
- huge operational headings
- random accent colors
- charts without a question
- icon-only critical navigation
- animation without informational value

## Brand changes

Differentiate:
- treatment fix: logo size, spacing, contrast, placement, correct variants
- brand refresh: palette, typography, iconography, surface language, visual personality
- identity redesign: actual logo/mark replacement or redraw

Treatment fixes can proceed when UI improvement was requested.

Broad brand refresh follows the selected autonomy mode.

Actual identity replacement requires explicit user intent.

## UI implementation boundaries

Prefer:

`Reuse -> Extend -> Refactor -> Add dependency`

Do not migrate frameworks solely for aesthetics.

Keep changes scoped and reviewable.

For existing products, preserve functional contracts while improving the presentation layer.

## Final validation

Before completion:
1. read `references/qa-checklist.md`
2. inspect the rendered UI when possible
3. test representative viewports, themes, directions, and states
4. run available tests, lint, type checks, accessibility checks, and relevant performance checks
5. compare meaningful redesigns against the baseline
6. report coverage, limitations, changes made, preserved behavior, and remaining approval items

If rendered inspection or a required check cannot be performed, say so explicitly.
