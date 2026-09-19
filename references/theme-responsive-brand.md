# Theme, Responsive, Brand, Icons, and Motion

## Existing Brand Audit

For existing products, do not assume the current brand treatment is correct simply because it already exists.

Audit:

- logo legibility and quality
- size, placement, clear space, and alignment
- contrast across Light/Dark surfaces
- responsive logo variants
- favicon/app icons
- palette quality and accessibility
- semantic color mapping
- typography/brand fit
- iconography consistency
- visual personality and product fit

Classify changes as:

- **Treatment fix** — preserve the identity; improve usage. May proceed when the user requested improvement.
- **Brand refresh** — change palette, typography, surface language, icon direction, or visual personality. Propose and approve before broad rollout.
- **Identity redesign** — alter/replace/redraw the actual logo or core mark. Requires explicit approval.

## Brand Assets

Inspect available variants:

- primary logo
- horizontal
- compact
- symbol-only
- light-background
- dark-background
- monochrome

Use only needed variants.

Validate logo in:

- sidebar
- collapsed navigation
- top bar
- authentication
- mobile header
- Light
- Dark

Preserve aspect ratio.

Do not accidentally stretch, crop, recolor, redraw, or distort an approved asset.

If the existing logo file is low quality, poorly suited to the interface, missing required variants, or the user explicitly requests a brand/identity improvement, recommend the needed correction.

Changing logo placement, size, clear space, theme variant, or responsive treatment is not the same as changing the identity and may be fixed as part of UI work.

Changing the actual logo artwork or core brand mark requires explicit approval before replacement.

## Favicon and App Icons

Prefer existing/supplied brand assets.

Where applicable configure:

- `favicon.ico`
- SVG/PNG favicon
- Apple touch icon
- PWA/app icons

If missing, surface the gap instead of inventing unrelated branding.

## Color and Palette Improvement

For existing products, audit whether the palette:

- provides sufficient contrast
- distinguishes interactive, neutral, and semantic roles
- works in both enabled themes
- avoids excessive unrelated accent colors
- supports charts/tables/forms without ambiguity
- aligns with the intended brand personality

Do not preserve a weak palette solely because it is existing code.

When the user asks for improvement:
- correct unsafe/inconsistent semantic colors directly when low risk
- for a global palette refresh, propose 2–3 directions and get approval
- migrate approved colors into semantic tokens rather than spreading new raw values

## Theme Architecture

New/major redesign default:

`Light + Dark`

Use semantic tokens such as:

- background
- surface
- surface-muted
- text-primary
- text-secondary
- border-default
- action-primary
- action-hover
- focus-ring
- status-success
- status-warning
- status-danger
- status-info

Do not spread raw brand hex values through components.

## Light QA

Review:

- background/surface hierarchy
- text contrast
- borders
- shadows/elevation
- status colors
- charts
- tables
- forms
- hover/focus/selected/disabled

## Dark QA

Review independently:

- background/surface hierarchy
- border visibility
- text and muted text
- brand/semantic colors
- charts
- tables
- forms
- dialogs/tooltips
- hover/focus/selected/disabled
- logo variant

Do not create Dark mode by simple inversion.

Avoid pure black everywhere unless intentionally required.

## Responsive Strategy

Responsive design is mandatory.

Review:

- Large Desktop
- Desktop
- Laptop
- Tablet
- Mobile

Use existing breakpoints where sensible.

Responsive changes may include:

- navigation
- grid/columns
- visible table fields
- filter presentation
- actions
- forms
- chart layout
- secondary panels
- sticky regions
- dialogs
- information priority

Do not merely shrink desktop UI.

## Responsive Priority

A discovery choice such as `Desktop-first` means priority, not exclusive support.

Even desktop-heavy products require intentional tablet/mobile behavior.

## Mobile Tables

Choose based on task:

- priority columns
- expandable rows
- summary/detail
- horizontal scroll
- dedicated record view

When column comparison is essential, horizontal scrolling can be superior to cards.

## Mobile Filters

Desktop filter bars may become:

- filter drawer
- bottom sheet
- dedicated filter screen

## Navigation

Choose based on destination count, depth, frequency, expertise, and width:

- Sidebar
- Compact Sidebar
- Top Navigation
- Hybrid

Mobile navigation may adapt.

## Icon System

Prefer one coherent family.

Use the existing icon set when suitable.

Avoid mixing outline, filled, emoji, and multiple libraries without a deliberate system.

Icons should improve recognition, not replace critical labels.

## Motion

Use motion to communicate state, hierarchy, continuity, or feedback.

For operational products normally use subtle motion.

Avoid decorative animation that delays access.

Respect reduced-motion preferences.

## Surface and Radius

Use a controlled system.

Possible surface characters:

- Flat
- Soft
- Bordered
- Refined

Possible radius characters:

- Sharp
- Subtle
- Rounded
- Soft

Avoid excessive radius and heavy static-card shadows.

Use shadow mainly for genuinely elevated/floating layers.
