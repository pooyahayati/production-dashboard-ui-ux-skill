# Changelog

All notable changes to **Production Dashboard UI/UX Skill** are documented here.

The project follows Semantic Versioning.

## [1.1.0] - 2026-09-19

### Added

- Dedicated existing-product audit and improvement workflow.
- Explicit support for completed/live projects without an existing `design-profile.md`.
- Observed Baseline workflow for preserving working product behavior while improving weak presentation.
- Audit matrix covering workflows, information architecture, visual hierarchy, components, tables, forms, responsive behavior, accessibility, RTL/LTR, and brand quality.
- Severity, impact, scope, confidence, and fix-type classification for audit findings.
- Safe-fix vs approval-required decision rules.
- Before/after comparison and regression review for existing products.
- Brand and visual-identity audit for logo treatment, palette, typography, iconography, Light/Dark behavior, and product fit.
- Controlled support for palette refresh, typography refresh, visual-language changes, and approved logo/identity redesign.
- Partial Rediscovery mode for strategic changes to existing products.

### Changed

- Existing visual styling is no longer preserved by default when it is a source of poor UX or weak product quality.
- Existing products can be audited and improved without forcing a full Design Discovery flow.
- Global brand, palette, navigation, and workflow changes now use explicit approval gates.
- QA now includes baseline/regression checks and brand/palette comparison.

## [1.0.0] - 2026-09-19

### Added

- Initial public release.
- Production-focused dashboard UI/UX workflow.
- Mandatory Design Discovery Wizard for new products and major redesigns.
- Persistent `design-profile.md` workflow.
- Design presets:
  - Minimal
  - Professional
  - Executive
  - Data-Dense
  - Modern SaaS
  - Premium
  - Technical
- Visual personality and information-density system.
- Conservative, Balanced, and Transformative redesign modes.
- Persian RTL support.
- English LTR support.
- Dynamic bilingual RTL/LTR architecture.
- Mixed-direction technical content handling.
- Local self-hosted font workflow.
- Persian/Latin font-pairing guidance.
- Logo, favicon, and application-icon requirements.
- Light/Dark theme architecture and QA.
- Responsive design requirements from large desktop to mobile.
- Dashboard-specific table, form, filter, KPI, chart, CRM, settings, authentication, and system-page guidance.
- Visual anti-pattern checks for generic AI-generated dashboard styling.
- Accessibility target based on WCAG 2.2 AA where practical.
- Final visual, UX, directionality, responsive, theme, accessibility, and engineering QA checklist.
- Codex UI metadata in `agents/openai.yaml`.
- Portable Agent Plugin manifest and mirrored `skills/` package.
- Privacy, terms, support, and public submission test materials.
- Automated validation for standalone-skill and plugin-package consistency.
