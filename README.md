# Production Dashboard UI/UX Skill

[![Validate](https://github.com/pooyahayati/production-dashboard-ui-ux-skill/actions/workflows/validate-skill.yml/badge.svg)](https://github.com/pooyahayati/production-dashboard-ui-ux-skill/actions/workflows/validate-skill.yml)
![Version](https://img.shields.io/badge/version-1.3.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A production-oriented Agent Skill for designing, auditing, improving, and redesigning dashboards, admin panels, CRM, analytics, and operational product interfaces.

Supports OpenAI Codex, Claude Code, Claude.ai / Claude Desktop, Persian RTL, English LTR, bilingual products, responsive UI, Light/Dark themes, reusable design systems, runtime design governance, personalization, branding, accessibility, performance, and existing-product regression-aware improvement.

## Quick start

### OpenAI Codex

Install from the canonical skill path:

```text
Use $skill-installer to install this skill from:
https://github.com/pooyahayati/production-dashboard-ui-ux-skill/tree/main/skills/production-dashboard-ui-ux-skill
```

Then use it explicitly:

```text
Use $production-dashboard-ui-ux-skill to audit and improve this dashboard.
```

Or:

```text
Use $production-dashboard-ui-ux-skill to redesign this dashboard.
```

Codex can also select the skill automatically when the request clearly matches its description.

### Claude.ai / Claude Desktop

1. Open the latest GitHub Release.
2. Download `production-dashboard-ui-ux-skill-claude-v1.3.0.zip`.
3. In Claude, enable **Code execution and file creation** if required.
4. Open **Customize → Skills**.
5. Choose **Upload a skill** and upload the ZIP.
6. Enable it.

Example:

```text
Use the Production Dashboard UI/UX Skill to audit and improve this dashboard.
```

### Claude Code

Download the same Claude-ready ZIP from the latest Release and extract the contained `production-dashboard-ui-ux-skill` folder into:

```text
~/.claude/skills/
```

Project-local installation can use:

```text
<project>/.claude/skills/
```

Then invoke:

```text
/production-dashboard-ui-ux-skill
```

## Existing projects

The skill is explicitly designed for completed or live products.

It can:

- establish an Observed Baseline
- audit current UI/UX
- report audit coverage instead of claiming unverified full coverage
- classify findings by severity, impact, scope, confidence, and fix type
- implement safe UI/UX improvements
- preserve business logic, permissions, validation, routing, API/data meaning, and user changes
- improve palette, typography, logo treatment, themes, responsive behavior, RTL/LTR, tables, forms, navigation, accessibility, and performance
- audit hard-coded presentation and design-system maintainability
- improve personalization, saved views, and Data Trust UX
- assess whether runtime owner customization is worth implementing
- perform before/after and regression-aware QA
- separate local treatment fixes from strategic redesign or identity changes

Example:

```text
Use $production-dashboard-ui-ux-skill to audit and improve this existing product.

Inspect the rendered UI and source code. Review UX, visual hierarchy,
responsive behavior, RTL/LTR, localization, accessibility, performance,
design-system changeability, personalization, data trust, palette,
typography, logo treatment, themes, tables, forms, and navigation.

Fix safe issues, preserve working product behavior and my existing changes,
and report audit coverage plus any remaining strategic decisions.
```

## Runtime UI Governance

Version 1.3 adds an optional architecture for products that need safe UI/UX changes after deployment.

It is **not mandatory for every project**.

The Skill should recommend an Owner UI/UX Control Center only when runtime customization has real product value, such as:

- white-label or multi-tenant products
- frequent brand/theme adjustments
- non-developer owners who need safe appearance controls
- multiple environments/tenants sharing design configuration
- operational defaults that need runtime adjustment
- meaningful user personalization requirements

Recommended precedence:

```text
Locked Product Constraints
        ↓
Design System Defaults
        ↓
Published Owner Config
        ↓
User Preferences
```

Lower layers cannot override protected constraints.

### Owner-only UI/UX Control Center

When appropriate, the product can include an owner-only control center for safe settings such as:

- approved logo variants
- favicon/app icon
- semantic brand colors
- default Light/Dark/System theme
- allowlisted font/typography preset
- Compact / Balanced / Comfortable density
- radius/surface preset
- motion level
- expanded/compact navigation presentation
- table row-density and page-size defaults
- approved chart palette
- locale/display defaults
- explicitly optional dashboard widgets

The owner panel must use real authorization at the server/trusted application boundary. Hiding a menu item is not sufficient.

### Safe publish lifecycle

Runtime design changes should follow:

```text
Edit Draft
   ↓
Preview
   ↓
Validate
   ↓
Publish
   ↓
Active Version
```

And support where appropriate:

- version history
- rollback
- audit log
- reset to defaults
- import/export
- schema versioning/migrations
- safe fallback if configuration fails to load

### What the owner panel must not expose

Do not expose generic runtime fields for:

- arbitrary CSS
- arbitrary JavaScript
- arbitrary HTML
- raw SQL
- API endpoints
- permission rules
- authentication behavior
- validation rules
- security controls
- unrestricted navigation/workflow logic

The feature is a safe presentation control plane, not a no-code application builder.

## Design System Architecture

For products expected to evolve, the Skill now prefers:

```text
Design Profile
    ↓
Design System Defaults
    ↓
Semantic Tokens
    ↓
Component Tokens
    ↓
Components
    ↓
Pages
```

This reduces hard-coded visual values and makes normal design changes safer.

A product should be able to change a common semantic color, density preset, typography preset, or theme behavior without editing unrelated pages one by one.

Runtime configuration should be:

- typed
- versioned
- bounded
- validated
- permissioned
- migration-aware
- reversible where appropriate

## User Personalization

Owner configuration and user preferences are separate layers.

Depending on product context, users may be allowed to persist:

- theme preference
- density
- sidebar state
- landing view
- table page size
- visible columns
- column order/width
- saved filters
- saved sorts
- saved views
- selected optional widgets
- date-range preference
- reduced-motion preference

Users can override only fields explicitly marked as user-configurable.

Preferences must not grant permissions or alter protected workflows.

## Saved Views and power-user UX

For high-frequency operational products, the Skill can recommend:

- private Saved Views
- shared team views
- owner-published default views
- quick filters
- bulk actions
- keyboard shortcuts
- command/search palette
- recent items
- inline editing where safe

Shared views require clear create/edit/delete permissions.

## Data Trust UX

Professional dashboards should help users understand whether the data can be trusted.

Where relevant, the Skill now reviews:

- last updated
- data freshness
- sync status
- data source
- timezone
- date range
- active filter scope
- metric definitions
- comparison baseline
- stale data
- partial data
- failed data sources
- drill-down to underlying records

A KPI should not look current and complete when the underlying data is stale or partial.

## Brand and visual refresh

The skill distinguishes:

- **Treatment fix** — logo placement, sizing, spacing, contrast, variants
- **Brand refresh** — palette, typography, iconography, surfaces, personality
- **Identity redesign** — actual logo/mark replacement

It may improve weak existing visual design. It does not preserve poor design merely because it already exists.

Actual identity replacement requires explicit user intent.

## Installation details

### Codex via skill-installer

The official Codex skill installer requires a path inside a GitHub repository. Use:

```text
https://github.com/pooyahayati/production-dashboard-ui-ux-skill/tree/main/skills/production-dashboard-ui-ux-skill
```

The installer currently installs into `$CODEX_HOME/skills` (default `~/.codex/skills`).

### Codex manual discovery locations

Current Codex documentation also supports user-level skills at:

```text
~/.agents/skills/
```

and repository skills at:

```text
<repo>/.agents/skills/
```

If installing manually, copy the canonical folder:

```text
skills/production-dashboard-ui-ux-skill/
```

into one of those locations.

## Updating

### Codex installed with $skill-installer

The installer intentionally does not overwrite an existing destination.

Ask Codex:

```text
Update $production-dashboard-ui-ux-skill to the latest version from:
https://github.com/pooyahayati/production-dashboard-ui-ux-skill/tree/main/skills/production-dashboard-ui-ux-skill

Remove the currently installed copy if necessary, then reinstall it with $skill-installer.
```

If doing it manually on macOS/Linux and using the installer's default destination:

```bash
rm -rf "${CODEX_HOME:-$HOME/.codex}/skills/production-dashboard-ui-ux-skill"
```

Then reinstall from the canonical GitHub path above.

If you maintain a manual Git checkout elsewhere, update that checkout with `git pull --ff-only` and copy or symlink the canonical skill folder into the supported Codex/Claude skills directory.

Restart Codex or start a new session if the updated skill is not immediately detected.

### Claude.ai / Claude Desktop

Download the newest Claude-ready ZIP from Releases and replace the older uploaded custom skill.

### Claude Code

Replace the installed skill folder with the folder from the newest Claude-ready ZIP.

## Usage examples

### New dashboard

```text
Use $production-dashboard-ui-ux-skill to design this new dashboard.
Recommend a design direction, establish a Design Profile, then implement it.
```

### Existing product — audit only

```text
Use $production-dashboard-ui-ux-skill to audit this existing product.
Do not modify code. Report coverage, prioritized findings, evidence, recommendations,
and whether the design system is easy to maintain and change.
```

### Existing product — delegated improvement

```text
Use $production-dashboard-ui-ux-skill to audit and improve this existing product.
Make reasonable design decisions without stopping for every approval.
Preserve business logic and report important decisions at the end.
```

### Owner UI/UX Control Center

```text
Use $production-dashboard-ui-ux-skill to design an owner-only UI/UX control center.

First determine whether runtime customization is appropriate for this product.
If it is, use typed allowlisted design configuration with semantic tokens,
Draft → Preview → Validate → Publish, version history, rollback, audit log,
safe fallback, and strict permission boundaries.

Do not expose arbitrary CSS, JavaScript, HTML, permissions, or business logic.
```

### User personalization and saved views

```text
Use $production-dashboard-ui-ux-skill to improve personalization for this dashboard.
Allow users to save useful preferences and views without overriding owner branding,
permissions, or locked product constraints.
```

### Persian RTL

```text
Use $production-dashboard-ui-ux-skill to improve this Persian RTL dashboard.
Audit mixed-direction technical values, tables, forms, navigation, typography,
localization, mobile behavior, and accessibility.
```

## Project structure

```text
production-dashboard-ui-ux-skill/
├── plugin.json
├── assets/
│   ├── logo.svg
│   └── composer-icon.svg
├── skills/
│   └── production-dashboard-ui-ux-skill/
│       ├── SKILL.md
│       ├── agents/
│       │   └── openai.yaml
│       └── references/
│           ├── accessibility.md
│           ├── dashboard-patterns.md
│           ├── design-presets.md
│           ├── design-system-architecture.md
│           ├── discovery-and-profile.md
│           ├── execution-safety.md
│           ├── existing-product-audit.md
│           ├── performance.md
│           ├── personalization-and-data-ux.md
│           ├── qa-checklist.md
│           ├── rtl-ltr-typography.md
│           ├── runtime-ui-governance.md
│           └── theme-responsive-brand.md
├── scripts/
│   ├── validate_release.py
│   └── package_release.py
├── evals/
├── submission/
├── .github/workflows/
├── README.md
├── CHANGELOG.md
├── VERSION
└── LICENSE
```

The canonical Skill source exists only under `skills/production-dashboard-ui-ux-skill/`. Release packages are generated from that source.

## Validation

Local release checks:

```bash
python3 scripts/validate_release.py
python3 scripts/package_release.py --output dist
```

CI additionally runs OpenAI's current `quick_validate.py` and a Codex installer smoke test on pushes to `main`.

Behavioral eval cases live in `evals/`. They are intentionally separate from structural validation because model behavior cannot be proven by regex or file checks.

## Releases

Latest release: **v1.3.0**

Release assets include:

- Claude-ready Skill ZIP
- OpenAI portable Plugin ZIP
- SHA-256 checksums

## Community and security

- [CONTRIBUTING.md](CONTRIBUTING.md)
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
- [SECURITY.md](SECURITY.md)
- [PRIVACY.md](PRIVACY.md)
- [TERMS.md](TERMS.md)
- [SUPPORT.md](SUPPORT.md)

## Author

**Pooya Hayati | پویا حیاتی**

[Pooyahayati.com](https://pooyahayati.com)

## License

MIT
