# Design Discovery and Design Profile

Use this reference for new products, broad redesigns, brand refreshes, or major visual/UX changes that need strategic design decisions.

For an existing product with no `design-profile.md`, do not automatically run full discovery for every improvement. First infer the current Observed Baseline using `references/existing-product-audit.md`. Use discovery only for unresolved strategic decisions.

## Discovery Modes

### Full Discovery
Use for new products or when the existing visual system is being substantially replaced.

### Partial Rediscovery
Use for an existing product when only selected strategic fields need reconsideration, such as:

- palette
- typography
- logo/brand direction
- density
- navigation
- Light/Dark strategy
- responsive priority
- visual personality

Keep unaffected decisions from the existing product or approved profile.

### Reuse Existing Profile
Use when `design-profile.md` exists and the requested work fits it.

## Discovery Strategy

Inspect first. Ask only unresolved questions.

For each meaningful choice:

- show `Recommended`
- give one short product-specific reason
- show alternatives
- include `Custom`
- include `Use your recommendation` when appropriate

Prefer one compact batch.

## Required Questions / Decisions

### 1. Product Context

Resolve product type, business domain, primary users/roles, key workflows, usage frequency, and operational vs analytical usage.

Useful categories:

- CRM
- Admin / Management System
- Analytics Dashboard
- Monitoring System
- Healthcare
- Education
- Financial
- Support
- Content Management
- Internal Tool
- SaaS
- Custom

### 2. Language and Direction

Offer:

- Persian — RTL
- English — LTR
- Persian + English — Dynamic RTL/LTR
- Other / Custom

### 3. Design Style

Offer:

- Minimal
- Professional
- Executive
- Data-Dense
- Modern SaaS
- Premium
- Technical
- Custom

Recommend one based on the product.

### 4. Visual Personality

Offer:

- Calm
- Serious
- Corporate
- Friendly
- Bold
- Premium
- Technical
- Custom

Style and personality are independent.

### 5. Information Density

Offer:

- Low
- Balanced
- High
- Use your recommendation
- Custom

Daily operational tools normally need more density than occasional executive views.

### 6. Design Freedom

Offer:

- Conservative — preserve structure; improve visual quality and usability
- Balanced — improve UX/UI while preserving core workflows
- Transformative — allow major structural redesign when justified
- Custom

Never treat `Transformative` as permission to change business logic.

### 7. Brand Assets and Brand Change Scope

Resolve whether the task is:

- preserve existing identity and improve usage
- refresh palette/typography/visual language
- redesign the actual logo/identity
- use supplied new brand assets
- Custom

For existing products, actual logo/identity replacement requires explicit approval.

Resolve:

- logo availability and variants
- favicon
- app/PWA icons where relevant
- brand colors
- brand guidelines
- custom illustrations/icons

Choices may include:

- I will provide logo and favicon
- Use existing project assets
- Logo exists; favicon is missing
- No brand assets yet
- Custom

### 8. Primary Font

Always resolve.

Offer:

- I will provide local font files
- Use existing project font
- Recommend Persian font
- Recommend English font
- Use system font stack
- Custom

For bilingual products also resolve:

- one bilingual family
- Persian family + Latin companion
- use your recommendation

### 9. Color Palette

If complete brand colors do not exist, propose 2–3 distinct palette directions.

For each preview show:

- primary
- accent
- background
- surface
- primary text

Always include `Custom palette`.

After selection, create full semantic tokens:

- primary/action
- accent
- neutral
- background
- surfaces
- border
- text-primary
- text-secondary
- success
- warning
- danger
- info
- focus ring

### 10. Theme

Default recommendation and requirement for new/major redesign:

- Light + Dark

Allow single-theme only when explicitly required.

### 11. Surface Character

Offer:

- Clean and flat
- Soft and modern
- Structured and bordered
- Premium and refined
- Use your recommendation
- Custom

Internally map to border, elevation, shadow, radius, surface hierarchy, and spacing.

### 12. Responsive Priority

Responsive support is mandatory. Ask only priority:

- Desktop-first
- Mobile-first
- Balanced
- Tablet-heavy
- Use your recommendation

### 13. Navigation

Recommend:

- Sidebar
- Compact Sidebar
- Top Navigation
- Hybrid
- Custom

Mobile navigation may adapt independently.

### 14. Localization

When relevant resolve:

- Gregorian / Jalali / localized calendar
- Persian / Latin / context-sensitive digits
- currency
- date/time formatting

Do not assume Jalali or Persian digits solely from Persian language.

### 15. Motion

Offer:

- None
- Subtle
- Expressive
- Use your recommendation

Operational software normally defaults to `Subtle`.

### 16. Authentication Scope

Determine which exist:

- Login
- Sign Up
- Forgot/Reset Password
- Email Verification
- OTP / 2FA
- Session Expired
- Account Locked
- Unauthorized

Do not invent flows the product does not have.

## Design Profile Schema

After discovery, show:

```text
DESIGN PROFILE

Product:
Primary Users:
Usage Pattern:
Primary Workflows:

Language:
Direction:
Localization:
Calendar:
Digits:

Design Style:
Visual Personality:
Information Density:
Design Freedom:

Primary Font:
Font Source:
Font Strategy:
Available Weights:
Latin Companion Font:

Brand Assets:
Logo:
Favicon:
App Icons:

Color Strategy:
Selected Palette:

Theme:
Surface:
Radius:
Icon System:
Motion:

Navigation:
Responsive Strategy:
Responsive Targets:

Data Visualization:
Accessibility Target:
Authentication Scope:
```

Omit irrelevant fields.

Mark inferred decisions as recommendations until approved.

After approval, write/update `design-profile.md`.
