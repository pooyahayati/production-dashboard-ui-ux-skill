# Theme, Responsive, Brand, Icons, and Motion

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

Do not stretch, crop, recolor, redraw, or distort without explicit approval.

## Favicon and App Icons

Prefer existing/supplied brand assets.

Where applicable configure:

- `favicon.ico`
- SVG/PNG favicon
- Apple touch icon
- PWA/app icons

If missing, surface the gap instead of inventing unrelated branding.

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
