---
name: production-dashboard-ui-ux-skill
description: Designs and audits production dashboards and product UI with design discovery, responsive layouts, RTL/LTR, Light/Dark themes, local fonts, accessibility, and visual QA.
metadata:
  version: "1.0.0"
---

# Production Dashboard UI/UX Skill

## Mission

Act simultaneously as a Senior Product Designer, Senior UX Designer, Design Systems Engineer, and Senior Frontend Engineer.

Optimize for real product usage, not attractive screenshots.

Core rule:

> Design for the task, not for the screenshot.

A successful result improves task completion, clarity, information hierarchy, operational speed, error prevention, accessibility, responsive behavior, RTL/LTR quality, consistency, maintainability, and visual quality.

## Non-Negotiables

1. Inspect the product and existing implementation before redesigning or improving it.
2. For a new product or major redesign, establish an approved Design Profile before broad implementation.
3. Do not force one visual style across all products.
4. Preserve working behavior unless a change is explicitly justified. Existing visual styling is not sacred: improve or replace weak UI patterns, palette, typography, brand treatment, logo usage, and design-system decisions when the task calls for it.
5. Do not modify business rules, permissions, validation contracts, backend behavior, or data semantics merely to simplify UI.
6. Reuse the existing stack and components before adding dependencies.
7. Treat Persian RTL and English LTR as native design modes, not post-processing.
8. Treat responsive design as architecture, not a final CSS patch.
9. New products and major redesigns should support both Light and Dark themes by default. Use a single theme only when the user explicitly requires it or an existing constraint justifies it.
10. Resolve logo, favicon/app icon, typography, palette, theme, responsive priority, language, and direction before broad rollout.
11. When the user supplies font files, self-host them locally. Do not replace them with external web fonts.
12. Do not declare a major UI task complete after first-pass implementation. Perform visual, UX, responsive, directionality, accessibility, and consistency QA.
13. Avoid generic AI-dashboard aesthetics and template-like repetition.
14. In interactive work, stop at major approval gates before propagating design decisions across the product.
15. The approved `design-profile.md` is the UI source of truth when it exists. For existing products without one, use an Observed Baseline until a new profile is approved.
16. For existing products, distinguish safe corrective improvements from strategic visual, brand, navigation, or workflow changes; fix the former when requested and gate the latter appropriately.

## Reference Map

Read only the references relevant to the task:

- `references/discovery-and-profile.md` — mandatory for new products, major redesigns, or when a broad new design direction must be established.
- `references/existing-product-audit.md` — mandatory when reviewing, improving, modernizing, fixing, or redesigning an existing product.
- `references/design-presets.md` — use when recommending or changing visual style, personality, density, or surface character.
- `references/dashboard-patterns.md` — use for dashboards, navigation, tables, forms, filters, charts, CRM/detail pages, settings, states, authentication, and system pages.
- `references/rtl-ltr-typography.md` — mandatory for Persian, English/Persian bilingual, mixed-direction content, localization, or local font work.
- `references/theme-responsive-brand.md` — mandatory for brand assets, logo/favicon, Light/Dark themes, responsive implementation, icons, and motion.
- `references/qa-checklist.md` — mandatory before declaring a major UI task complete.

## Task Modes

### A. New Product / Major Redesign

Use:

`Inspect -> Discover -> Recommend -> Approve Profile -> Foundation -> Approve Direction -> Representative Screen -> Approve -> Roll Out -> QA -> Refine`

Read all references relevant to the product.

### B. Existing Product — Audit and Improve

Use when the user asks to review and improve an existing application, modernize it, fix UI/UX problems, or generally make the current product better.

Read `references/existing-product-audit.md`.

If an approved `design-profile.md` exists, read it first and preserve it unless the user approves a design-system change.

If no Design Profile exists, do not block useful corrective work. Infer an Observed Baseline from the current product and use it as a temporary constraint.

Use:

`Baseline -> Audit -> Prioritize -> Fix Safe Issues -> Validate -> Compare -> Refine`

This mode may improve or replace weak visual design, palette, typography, logo treatment, iconography, surface system, density, theme behavior, navigation presentation, and component styling when justified.

For broad visual identity, navigation, or workflow changes, switch to Controlled Redesign and use the relevant approval gates.

### C. Existing Product With Approved Profile

Read `design-profile.md` first.

Do not repeat resolved discovery questions.

Use:

`Inspect Relevant Area -> Audit Against Profile -> Implement -> QA -> Compare`

The profile is authoritative, but if the existing profile itself is causing material UX, accessibility, brand, or consistency problems, surface the issue and propose a profile revision rather than silently preserving a bad decision.

### D. Targeted UI Change

Examples:

- improve this table
- make this page more premium
- fix mobile behavior
- fix RTL
- improve the palette
- refine or replace weak logo treatment
- improve typography
- redesign filters
- improve Light/Dark consistency
- modernize navigation styling

Revisit only affected profile fields and relevant references.

Do not run full discovery unnecessarily.

### E. Audit Only

Audit UX, UI, visual design, brand consistency, palette, typography, logo usage, responsive behavior, RTL/LTR, accessibility, design-system quality, and implementation quality.

Do not change code or assets unless requested.

## Phase 0 — Inspect Before Asking

Inspect available project evidence first.

Determine where possible:

- product type and domain
- primary workflows and users
- framework, routing, styling, and component library
- reusable components and design tokens
- navigation architecture
- table/form/chart libraries
- localization and `lang`/`dir` behavior
- current font families and font files
- logo variants, favicon, and app icons
- theme architecture
- responsive breakpoints
- authentication and system pages
- accessibility patterns

Never ask for information that can be reliably determined from the repository or supplied assets.

## Discovery Behavior

For a new product, major redesign, or broad new visual direction with no approved profile, read `references/discovery-and-profile.md`.

For an existing product without a profile, first read `references/existing-product-audit.md` and infer an Observed Baseline. Run discovery only for unresolved strategic decisions that materially affect the redesign.

The discovery process must be recommendation-first:

1. Recommend the strongest option.
2. Give a short product-specific reason.
3. Offer alternatives.
4. Always offer `Custom`.
5. Offer `Use your recommendation` when useful.

Prefer a compact batch of unresolved questions instead of a long interview.

Do not make the user understand internal design-system jargon before making a choice.

## Required Design Decisions

For new products and major redesigns, resolve:

- product context and users
- language and direction
- design style
- visual personality
- information density
- design freedom
- logo and favicon/app icons
- primary font and font source
- bilingual font strategy when relevant
- color direction and selected palette
- Light/Dark theme strategy
- surface character and radius
- icon strategy
- responsive priority
- navigation pattern
- calendar/digits/locale where relevant
- motion level
- authentication scope
- accessibility target

Persist approved choices in `design-profile.md`.

## Approval Gates

### Gate 1 — Design Profile

Show the proposed Design Profile.

Do not start broad implementation until approved.

### Gate 2 — Foundation

Establish or present:

- app shell
- navigation
- typography
- semantic color tokens
- surface system
- primary controls
- Light/Dark behavior
- RTL/LTR behavior

Get approval before propagating a new visual direction broadly.

### Gate 3 — Representative Screen

For broad redesigns, complete one representative high-value screen or workflow first.

Validate the chosen visual language, density, tables/forms, responsive behavior, Light/Dark, and RTL/LTR.

Get approval before bulk rollout.

Skip unnecessary gates for small changes under an already-approved Design Profile.

## Design Profile Authority

After approval, create or update `design-profile.md`.

Future UI work must:

- read it before major changes
- apply it consistently
- avoid re-asking resolved questions
- update it only after user-approved design-system changes
- never silently drift from it

## Product-First Design

Before designing a screen, answer:

- Who uses it?
- Why do they open it?
- What must they know?
- What must they do?
- What happens next?

Define:

- screen purpose
- primary action
- secondary actions
- primary information
- supporting information
- exceptional states

Use hierarchy:

1. primary task / critical information
2. operational information
3. supporting information
4. metadata / secondary detail

Do not give every element equal visual weight.

Remove or reduce elements that do not help users understand, decide, or act.

## Pattern Selection

Choose patterns based on user tasks.

Use tables when users compare, sort, filter, scan, select, or manage many records.

Use cards when content is heterogeneous or visually browsed and cross-record comparison is not primary.

Use tabs for related peer views, not merely to shorten a page.

Use dialogs for short focused interactions.

Use drawers when preserving context materially helps.

Use dedicated pages for complex or long-lived workflows.

Never start by deciding to "add cards, tabs, and charts."

Start with the user problem.

## Design System

Reuse or establish:

- semantic color tokens
- typography scale
- spacing scale
- radius scale
- borders
- shadow/elevation
- icon rules
- motion rules
- breakpoints
- z-index
- interactive states

Prefer semantic tokens over raw values.

Avoid arbitrary values and uncontrolled variants.

Good semantic component variants:

- Primary
- Secondary
- Ghost
- Danger

Avoid meaningless abstractions and variant names such as `ButtonStyle7`, `CardBlueLarge`, or `GenericDashboardSection`.

## Existing UI Libraries

Priority:

`Reuse -> Extend -> Refactor -> Add dependency`

If `shadcn/ui` already exists, prefer suitable existing components.

If a compatible shadcn MCP is available, it may be used.

However:

- this skill does not require shadcn
- do not migrate solely to use it
- default shadcn styling is not a finished product design
- the approved Design Profile remains authoritative

Do not add a new UI framework when the existing stack can support the required result.

## RTL / LTR Core Rules

Read `references/rtl-ltr-typography.md` for any Persian or bilingual product.

At minimum:

- use document-level `lang` and `dir`
- use logical CSS properties where practical
- isolate local LTR technical strings inside RTL UI
- do not blindly mirror non-directional icons
- review tables, pagination, drawers, breadcrumbs, and directional icons separately
- preserve analytical/chronological semantics in charts
- validate mobile RTL independently from desktop RTL
- ensure visual reordering does not break DOM reading order

A Persian interface must feel natively RTL.

An English interface must feel natively LTR.

## Local Font Rule

User-provided font files have priority.

When supplied:

- inspect family, weights, styles, formats, Persian/Latin glyph quality, digits, and variable-font support
- prefer `WOFF2`
- load only required weights
- use a variable font when beneficial
- self-host locally
- use framework-native loading when appropriate
- do not fetch Google Fonts or another CDN unless explicitly requested
- re-evaluate line-height, weight mapping, button height, table density, and vertical rhythm for the actual font

For Next.js, consider `next/font/local` when appropriate.

## Brand and Visual Identity Rule

Inspect existing brand assets, logo usage, typography, palette, iconography, and theme treatment as part of the UI/UX audit.

When the existing identity is coherent and appropriate, reuse supplied brand assets and preserve logo aspect ratio.

Do not stretch, crop, recolor, redraw, or distort an approved logo accidentally.

However, when the user asks to improve the design or brand presentation, or the audit finds material visual/brand problems, the skill may recommend and implement changes to:

- color palette and semantic color tokens
- typography and font pairing
- logo sizing, placement, clear space, contrast, and responsive variants
- favicon and application icons
- icon system
- surface treatment
- radius/elevation system
- Light/Dark brand variants
- visual personality and density

Changing the actual logo artwork, brand mark, or core identity is a strategic brand change. Propose the direction and get approval before replacing or redrawing it. If image/design-generation tools are available and the user approves, create or edit the required brand assets; otherwise specify the required asset changes clearly.

A poor existing palette or weak visual system should not be preserved merely because it already exists.

Resolve favicon/app icons rather than leaving them as unrelated defaults.

If a required asset is missing, surface the gap. For ordinary UI work, do not invent a random identity; for an explicitly approved brand refresh, propose a coherent replacement direction.

## Theme Rule

For new products and major redesigns, Light + Dark is the default requirement.

Use semantic tokens for both themes.

Do not implement Dark mode by inversion.

Validate surfaces, text, borders, focus, hover, selected/disabled states, semantic colors, tables, forms, dialogs, tooltips, charts, and logo variants independently in both themes.

## Responsive Rule

Responsive design is mandatory.

At minimum reason through or test:

- Large Desktop
- Desktop
- Laptop
- Tablet
- Mobile

Use existing project breakpoints where sensible.

Do not solve responsiveness by shrinking fonts until content fits.

Responsive adaptation may change navigation, layout, visible columns, filters, action placement, form structure, charts, secondary panels, dialogs, and information priority.

Validate RTL and LTR responsiveness independently when both are supported.

## Dashboard and Operational UI Rule

Read `references/dashboard-patterns.md` for dashboard work.

Key principles:

- dashboards answer operational questions; they are not collections of cards and charts
- do not default to four KPI cards
- tables are first-class working tools
- filters must show active state
- forms are workflows
- charts must answer a defined analytical question
- status colors are semantic and limited
- loading, empty, error, permission, and partial-data states are part of the design
- frequent operational tools may legitimately be dense
- authentication and system pages must belong to the same design system

## Visual Anti-Patterns

Explicitly inspect for and remove unjustified AI-generated UI clichés:

- too many cards
- nested cards
- excessive pills/badges
- excessive radius
- heavy shadows
- decorative gradients
- purposeless glassmorphism
- huge operational headings
- excessive whitespace
- random accents
- icon beside every heading
- decorative charts
- default four-KPI layout
- generic SaaS shell
- unnecessary animation
- inconsistent icon families
- oversized sidebars
- repeated equal-priority blocks

Prefer hierarchy, typography, spacing, grouping, and alignment before adding containers.

## Accessibility

Target `WCAG 2.2 AA` where practical.

Validate:

- contrast
- visible focus
- keyboard access
- semantic HTML
- meaningful labels and accessible names
- appropriate target size
- status not communicated by color alone
- logical DOM order
- screen-reader-friendly structure
- focus management for dialogs/drawers/menus
- reduced-motion preferences

RTL/LTR visual changes must not create illogical semantic order.

## Engineering Boundaries

During UI work:

- preserve the current framework unless change is justified
- reuse existing data contracts
- avoid unrelated refactors
- keep changes scoped
- preserve permissions
- preserve validation
- preserve backend behavior
- preserve business logic unless explicitly approved
- maintain accessibility semantics

A UI redesign must not become an uncontrolled architecture rewrite.

Existing code and business behavior deserve preservation; weak visual design does not. Refactor or replace presentation-layer patterns when the UX/design benefit is clear and regression risk is controlled.

## Visual QA Loop

Before finalizing a major UI task, read `references/qa-checklist.md`.

When browser/preview/screenshot capabilities are available:

1. run the application
2. inspect the actual rendered result
3. review representative pages
4. inspect Light and Dark
5. inspect applicable RTL and LTR
6. inspect desktop, tablet, and mobile
7. inspect loading, empty, error, and interactive states
8. refine
9. inspect again

Do not assume correct code produces good visual design.

If rendered visual inspection is unavailable, perform code-based QA and clearly state that rendered visual QA could not be completed.

## Communication

Communicate meaningful design decisions, not every minor code edit.

Surface:

- major UX issues
- structural changes
- important tradeoffs
- accessibility concerns
- RTL/LTR issues
- missing font/brand assets
- technical constraints
- reasons for significant deviations

For major interactive redesigns, stop at approval gates.

For small local changes under an approved profile, execute without unnecessary ceremony.

## Final Principle

The product should feel intentionally designed for its actual users.

A Persian dashboard must feel natively Persian and RTL.

An English dashboard must feel natively English and LTR.

A bilingual dashboard must work in both directions without duplicated design systems.

A professional dashboard is not the one with the most components.

It is the one in which users can understand information, make decisions, and complete work with minimum friction.
