# RTL, LTR, Localization, and Typography

## Direction Architecture

Prefer document-level language and direction:

```html
<html lang="fa" dir="rtl">
<html lang="en" dir="ltr">
```

For runtime language switching, update direction at the document/app-shell level.

Prefer one shared direction-aware component system over separate RTL and LTR component trees.

## Logical CSS

Prefer logical properties:

- `margin-inline-start/end`
- `padding-inline-start/end`
- `inset-inline-start/end`
- `border-inline-start/end`
- `text-align: start/end`

Avoid hard-coded left/right when a logical property works.

## Mixed-Direction Content

A Persian UI often contains LTR values:

- email
- URL
- domain
- IP
- API key/token
- username
- file path
- slug
- version
- model name
- technical ID
- code

Use local isolation when needed:

- `dir="ltr"`
- `bdi`
- `unicode-bidi: isolate`

Do not use whitespace hacks.

Prevent broken punctuation, parentheses, symbols, phone numbers, URLs, versions, and technical identifiers.

## Directional Icons

Usually do not mirror:

- settings
- user
- search
- calendar
- bell
- trash
- download/upload
- database

Review semantic directional icons:

- back/forward
- previous/next
- chevrons
- expand/collapse direction

## RTL Tables

For Persian tables:

- primary descriptive columns normally align to the RTL reading edge
- technical/numeric values may use local LTR
- sticky columns must respect direction
- sort indicators must remain aligned
- pagination must follow RTL interaction conventions
- horizontal scrolling must remain understandable
- actions must stay consistent

Do not reverse data semantics.

## RTL Forms

Persian text inputs are usually RTL.

Technical fields are usually LTR.

Labels, errors, prefixes, and suffixes must remain stable.

## Charts

Localize labels, legends, tooltips, and annotations.

Do not reverse chronological axes merely because the interface is RTL.

## Responsive Direction

Validate independently:

- mobile navigation
- drawer side/direction
- back controls
- breadcrumbs
- pagination
- table overflow
- sticky columns
- form alignment
- floating actions
- modal positioning

Desktop RTL correctness does not guarantee mobile RTL correctness.

## Accessibility

Visual mirroring must not create an illogical DOM order.

Keyboard navigation and screen-reader order should remain semantic.

## Local Font Strategy

When user-provided font files exist:

1. inspect family, weights, styles, formats, variable-font support
2. evaluate Persian glyphs, Latin glyphs, digits, punctuation
3. prefer `WOFF2`
4. load only required weights
5. prefer variable font when beneficial
6. self-host locally
7. use framework-native font loading where appropriate
8. set useful fallbacks
9. use `font-display: swap` or framework-equivalent behavior when relevant

Do not load from Google Fonts/CDN unless explicitly requested.

For Next.js, consider `next/font/local`.

After changing font, re-evaluate:

- line height
- type scale
- weight mapping
- button/control height
- table density
- vertical rhythm

## Bilingual Typography

Choose either:

- one high-quality bilingual family
- Persian family + compatible Latin companion

Match stroke density, visual scale, weights, and line height.

Do not assume a strong Persian font has equally strong Latin forms.

## Digits, Dates, Calendar

When relevant explicitly determine:

- Persian / Latin / context-sensitive digits
- Gregorian / Jalali / localized calendar
- currency format
- date/time format
- thousand/decimal separators

Technical values may remain Latin even inside a Persian interface.

Do not mix digit systems randomly.
