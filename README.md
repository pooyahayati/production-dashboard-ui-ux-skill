# Production Dashboard UI/UX Skill

[![Validate Skill](https://github.com/pooyahayati/production-dashboard-ui-ux-skill/actions/workflows/validate-skill.yml/badge.svg)](https://github.com/pooyahayati/production-dashboard-ui-ux-skill/actions/workflows/validate-skill.yml)
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)


A production-oriented Agent Skill for designing, auditing, redesigning, and implementing professional dashboard and product interfaces with **responsive design, Persian RTL, English LTR, bilingual UI architecture, Light/Dark themes, local fonts, brand assets, dashboard UX patterns, and visual QA**.

Designed for use with **OpenAI Codex**, **Claude Code**, **Claude.ai / Claude Desktop**, and other tools that support the Agent Skills format.

## Quick start

### OpenAI Codex

The fastest way to install and use the skill with Codex is:

```text
Use $skill-installer to install this skill from:
https://github.com/pooyahayati/production-dashboard-ui-ux-skill
Use $production-dashboard-ui-ux-skill to redesign this dashboard.
```

After installation, invoke it explicitly with:

```text
Use $production-dashboard-ui-ux-skill ...
```

### Claude Code

Install the skill globally for all Claude Code projects:

```bash
git clone --depth 1 https://github.com/pooyahayati/production-dashboard-ui-ux-skill.git \
  "$HOME/.claude/skills/production-dashboard-ui-ux-skill"
```

Or install it only for the current project:

```bash
git clone --depth 1 https://github.com/pooyahayati/production-dashboard-ui-ux-skill.git \
  ".claude/skills/production-dashboard-ui-ux-skill"
```

Then invoke it directly in Claude Code:

```text
/production-dashboard-ui-ux-skill
```

Or describe the task naturally, for example:

```text
Use the Production Dashboard UI/UX Skill to redesign this dashboard.
```

### Claude.ai / Claude Desktop

1. Download the Claude-ready ZIP: [production-dashboard-ui-ux-skill-claude-v1.0.0.zip](https://github.com/pooyahayati/production-dashboard-ui-ux-skill/releases/download/v1.0.0/production-dashboard-ui-ux-skill-claude-v1.0.0.zip)
2. In Claude, make sure **Code execution and file creation** is enabled.
3. Open **Customize → Skills**.
4. Click **+ → Create skill → Upload a skill**.
5. Upload the ZIP and enable the skill.
6. Ask Claude to use it for your dashboard task.

Example:

```text
Use the Production Dashboard UI/UX Skill to redesign this dashboard.
```

For a new dashboard or a major redesign, the skill inspects the project, establishes a Design Profile, and then applies the approved UI/UX direction.

## Why this skill exists

Coding agents can build functional dashboards quickly, but the default result is often visually generic, overly card-based, inconsistent, or weak in production UX.

This skill adds a structured product-design workflow before and during implementation. It helps an agent decide **what the interface should be**, not only how to code it.

It is intended for:

- Admin panels
- SaaS dashboards
- CRM systems
- Healthcare software
- Education platforms
- Financial and operational tools
- Analytics dashboards
- Monitoring systems
- Internal business applications
- Bilingual Persian/English products

## Key capabilities

### Design Discovery Wizard

For a new product or major redesign, the skill first inspects the project, then resolves only the missing design decisions.

It recommends options and lets the user choose or provide a custom direction.

The resulting `design-profile.md` becomes the UI source of truth for later work.

### Multiple design directions

Built-in starting profiles:

- Minimal
- Professional
- Executive
- Data-Dense
- Modern SaaS
- Premium
- Technical

These are not fixed templates. Each can be combined with different visual personalities, information densities, surface styles, navigation patterns, palettes, and motion levels.

### Persian RTL + English LTR

The skill treats direction as part of the product architecture.

It covers:

- document-level `lang` and `dir`
- logical CSS properties
- mixed Persian/English content
- LTR technical values inside RTL interfaces
- direction-aware navigation and icons
- RTL tables and pagination
- responsive RTL behavior
- bilingual typography
- Jalali/Gregorian and digit strategies where applicable

### Local fonts

If font files are supplied, the skill prioritizes local self-hosting.

It checks:

- font family
- available weights
- Persian and Latin glyph quality
- digits and punctuation
- variable-font support
- framework-native loading

External font CDNs are not used unless explicitly requested.

### Brand assets

Logo, favicon, and application icons are treated as first-class product requirements.

The skill validates relevant brand variants across:

- Light theme
- Dark theme
- sidebar
- collapsed navigation
- authentication
- mobile header

### Light and Dark themes

For new products and major redesigns, dual-theme support is the default.

Themes use semantic tokens rather than component-level hard-coded colors.

Dark mode is designed independently rather than generated through simple inversion.

### Responsive product design

The skill covers:

- Large Desktop
- Desktop
- Laptop
- Tablet
- Mobile

Responsive behavior may restructure navigation, filters, forms, tables, dialogs, panels, and information priority instead of merely shrinking the desktop UI.

### Dashboard-specific UX

Includes guidance for:

- application shells
- sidebars and navigation
- page headers and actions
- KPIs
- data tables
- search and filters
- bulk actions
- forms
- charts
- CRM detail pages
- settings
- empty/loading/error states
- authentication flows
- system pages

### Visual QA

A major UI task is not considered complete after the first implementation pass.

The skill requires review of:

- hierarchy
- typography
- spacing
- density
- brand consistency
- Light/Dark
- RTL/LTR
- responsive behavior
- accessibility
- loading/empty/error states
- maintainability

## Structure

```text
production-dashboard-ui-ux-skill/
├── plugin.json
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── dashboard-patterns.md
│   ├── design-presets.md
│   ├── discovery-and-profile.md
│   ├── qa-checklist.md
│   ├── rtl-ltr-typography.md
│   └── theme-responsive-brand.md
├── skills/
│   └── production-dashboard-ui-ux-skill/
│       ├── SKILL.md
│       ├── agents/
│       └── references/
├── submission/
│   ├── TEST_CASES.md
│   └── SUBMISSION_CHECKLIST.md
├── PRIVACY.md
├── TERMS.md
├── SUPPORT.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
└── VERSION
```

`SKILL.md` contains the core workflow and routes the agent to detailed references only when they are relevant. This keeps context usage lower than a single monolithic instruction file.

## Availability

The repository supports two distribution modes:

- **Standalone Agent Skill** — usable from supported local skill environments such as ChatGPT Desktop, Codex CLI, and the Codex IDE extension.
- **Portable Agent Plugin package** — the repository also contains a root `plugin.json` and the mirrored skill under `skills/`, following the Agent Plugins package layout.

The GitHub repository is public, so anyone can inspect, fork, clone, and install the standalone skill.

Public discovery inside the universal ChatGPT + Codex Plugin Directory is a separate OpenAI review/publishing step. Submission materials are prepared under `submission/`.

## Installation

### OpenAI Codex

Ask Codex to install directly from GitHub:

```text
Use $skill-installer to install this skill from:
https://github.com/pooyahayati/production-dashboard-ui-ux-skill
```

Manual user-level installation:

```bash
git clone https://github.com/pooyahayati/production-dashboard-ui-ux-skill.git \
  "$HOME/.agents/skills/production-dashboard-ui-ux-skill"
```

For repository-specific use:

```text
<repo>/.agents/skills/production-dashboard-ui-ux-skill/
```

### Claude Code

Claude Code discovers filesystem-based Skills automatically.

Personal installation for all projects:

```bash
git clone --depth 1 https://github.com/pooyahayati/production-dashboard-ui-ux-skill.git \
  "$HOME/.claude/skills/production-dashboard-ui-ux-skill"
```

Project-only installation:

```bash
git clone --depth 1 https://github.com/pooyahayati/production-dashboard-ui-ux-skill.git \
  ".claude/skills/production-dashboard-ui-ux-skill"
```

Claude Code can use the skill automatically when relevant, or you can invoke it directly:

```text
/production-dashboard-ui-ux-skill
```

### Claude.ai / Claude Desktop

Custom Skills can be uploaded as ZIP files.

1. Download [production-dashboard-ui-ux-skill-claude-v1.0.0.zip](https://github.com/pooyahayati/production-dashboard-ui-ux-skill/releases/download/v1.0.0/production-dashboard-ui-ux-skill-claude-v1.0.0.zip) from the v1.0.0 Release.
2. Enable **Code execution and file creation** in Claude if it is not already enabled.
3. Go to **Customize → Skills**.
4. Click **+ → Create skill → Upload a skill**.
5. Upload the ZIP.
6. Enable the skill and use it naturally in your conversations.

### Portable Agent Plugin package

The repository is also packaged as a portable skills-only Agent Plugin:

```text
plugin.json
skills/production-dashboard-ui-ux-skill/
```

This package is prepared for local plugin testing and public Plugin Directory submission.

## Usage

Codex may discover the skill automatically when the request matches its description.

You can also invoke it explicitly:

```text
Use $production-dashboard-ui-ux-skill to redesign this dashboard.
```

For a new project:

```text
Use $production-dashboard-ui-ux-skill for this dashboard project.
Inspect the current frontend first, run the design discovery workflow,
recommend the best design profile, and wait for my approval before
implementing the new visual direction.
```

For an existing Persian dashboard:

```text
Use $production-dashboard-ui-ux-skill to audit and redesign this dashboard.
The product is Persian and must be native RTL.
Preserve the business logic and existing API contracts.
```

For a targeted improvement:

```text
Use $production-dashboard-ui-ux-skill to improve this data table and filters.
Reuse the existing design profile and do not redesign unrelated pages.
```

## Design Profile

For major design work, the skill creates or updates:

```text
design-profile.md
```

Typical fields include:

```text
Product:
Primary Users:
Language:
Direction:
Design Style:
Visual Personality:
Information Density:
Design Freedom:
Primary Font:
Font Source:
Color Strategy:
Theme:
Surface:
Radius:
Navigation:
Responsive Strategy:
Calendar:
Digits:
Motion:
Logo:
Favicon:
Authentication Scope:
Accessibility Target:
```

This prevents later pages from drifting into different visual systems.

## Design principles

The skill follows several strong defaults:

- Design for the task, not for the screenshot.
- Product usability has priority over decoration.
- Do not default to card grids and four KPI blocks.
- Tables are first-class productivity tools.
- RTL is architecture, not a CSS patch.
- Responsive design may require structural adaptation.
- Light/Dark themes must be independently validated.
- User-provided fonts and brand assets take priority.
- Existing framework and business logic should be preserved unless change is justified.
- A rendered visual QA pass is preferred whenever the environment supports it.

## Compatibility

The package follows the Agent Skills structure:

- required `SKILL.md`
- YAML frontmatter with `name` and `description`
- optional `agents/openai.yaml`
- conditional `references/`

It is designed for Codex skill discovery and progressive loading.

## Version

Current release:

```text
v1.0.0
```

See [CHANGELOG.md](CHANGELOG.md) for release history.

## Contributing

Issues, design-pattern improvements, RTL/LTR edge cases, accessibility improvements, and production dashboard examples are welcome.

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Community and security

- Report bugs and feature requests using the GitHub issue templates.
- See [CONTRIBUTING.md](CONTRIBUTING.md) before proposing changes.
- See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for participation expectations.
- See [SECURITY.md](SECURITY.md) for security reporting guidance.
- See [PRIVACY.md](PRIVACY.md) for privacy information.
- See [TERMS.md](TERMS.md) for terms of use.
- See [SUPPORT.md](SUPPORT.md) for support channels.

## License

MIT License. See [LICENSE](LICENSE).

## Author

Created and maintained by:

**Pooya Hayati | پویا حیاتی**

[Pooyahayati.com](https://pooyahayati.com)
