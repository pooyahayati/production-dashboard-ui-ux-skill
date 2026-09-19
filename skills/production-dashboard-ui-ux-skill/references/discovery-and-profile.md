# Design Discovery and Design Profile

Use for new products, major redesigns, or strategic changes to an existing visual system.

Do not run full discovery when a narrow existing-product fix can be resolved from the current baseline.

## Modes

### Full Discovery

Use for new products or substantial system replacement.

### Partial Rediscovery

Use when only selected strategic fields need reconsideration, such as:

- palette
- typography
- logo or brand direction
- density
- navigation
- theme strategy
- responsive priority
- visual personality

### Reuse Existing Profile

Use when an approved `design-profile.md` exists and remains appropriate.

## Recommendation-first discovery

For unresolved strategic decisions:

1. recommend the strongest option
2. give a short product-specific reason
3. offer a small number of alternatives
4. offer Custom
5. accept "use your recommendation" as delegated approval where appropriate

Inspect repository and assets before asking questions.

## Decisions to resolve when relevant

- product and domain
- user roles
- high-frequency workflows
- operational vs analytical usage
- language and direction
- visual style
- personality
- density
- design freedom
- brand and logo scope
- font and font source
- bilingual font strategy
- palette
- Light/Dark
- surface and radius
- icon system
- responsive priority
- navigation
- date, time, digits, currency, and calendar
- motion
- auth and system-page scope
- accessibility target

## Brand change scope

Explicitly distinguish:

- preserve identity and improve treatment
- refresh palette, typography, or visual language
- redesign actual logo or identity
- use supplied new brand assets

Actual identity replacement requires explicit user intent.

## Design Profile schema

Use a concise Markdown or YAML-like structure. Include provenance so future work can tell what was observed vs approved.

Example:

```yaml
profile_version: 1
skill_version: 1.2.0
status: approved
updated_at: 2026-09-20

product:
  type: operational-dashboard
  users: [admin, operator]
  primary_workflows:
    - review queue
    - update record

direction:
  languages: [fa, en]
  rtl: true
  ltr: true

visual:
  style: professional
  personality: calm
  density: high
  freedom: balanced

brand:
  change_scope: treatment-only
  logo_source: existing
  palette: approved-semantic-tokens
  typography: local-font

theme:
  modes: [light, dark]

responsive:
  priority: desktop-first
  supported: [large-desktop, desktop, laptop, tablet, mobile]

decisions:
  - field: visual.density
    value: high
    source: user-approved
  - field: brand.logo_source
    value: existing
    source: observed-baseline

locked_constraints:
  - preserve authentication flow
  - do not change brand mark

open_questions: []
```

## Status

Use:

- `draft` while strategic choices remain unresolved
- `approved` after user approval or explicit delegated authority

## Decision source

Useful values:

- user-provided
- user-approved
- delegated-recommendation
- observed-baseline
- existing-profile

Do not represent an inferred decision as user-approved.

## Updates

Before major UI work:

- read the profile
- respect locked constraints
- avoid re-asking resolved questions
- update only affected strategic fields
- preserve provenance
- update `skill_version` when materially revising the profile with a newer Skill
