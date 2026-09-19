# Final QA Checklist

Use before declaring a major UI task complete.

## Existing Product Baseline and Regression

For existing-product work:

- [ ] A baseline was inspected before meaningful changes.
- [ ] Representative existing workflows were identified.
- [ ] Business logic, permissions, validation, routing, and data semantics remain intact unless explicitly approved.
- [ ] Before/after comparison was performed for meaningful redesign work.
- [ ] Available tests, type checks, linters, and regression checks were run where practical.
- [ ] Any checks that could not be run are stated explicitly.

## Product and UX

- [ ] Screen purpose and primary action are clear.
- [ ] Critical information has appropriate visual priority.
- [ ] Common workflows are efficient.
- [ ] Empty, loading, and error states are useful.
- [ ] User feedback is visible for asynchronous operations.

## Design System

- [ ] Typography, spacing, colors, borders, radius, and elevation are consistent.
- [ ] Existing components and patterns are reused where appropriate.
- [ ] Generic dashboard styling has been reduced.

## Brand and Typography

- [ ] Existing logo/brand treatment was audited rather than blindly preserved.
- [ ] Logo and favicon integration are correct.
- [ ] Relevant logo variants work across enabled themes and responsive contexts.
- [ ] Palette changes improve contrast, semantic clarity, and brand consistency.
- [ ] Strategic brand/identity changes were explicitly approved before broad rollout.
- [ ] Supplied local font files are self-hosted and optimized.
- [ ] Persian, Latin, and mixed-script text are readable when applicable.

## Theme

- [ ] Light theme is reviewed.
- [ ] Dark theme is reviewed unless explicitly out of scope.
- [ ] Forms, tables, charts, dialogs, and semantic colors work in enabled themes.

## Responsive

- [ ] Desktop, laptop, tablet, and mobile behavior are reviewed.
- [ ] Navigation, tables, filters, forms, and dialogs adapt intentionally.
- [ ] Important content is not clipped or hidden unintentionally.

## RTL / LTR

- [ ] Persian RTL is reviewed when applicable.
- [ ] English LTR is reviewed when applicable.
- [ ] Mixed-direction values remain readable.
- [ ] Directional icons, tables, pagination, breadcrumbs, and drawers behave correctly.
- [ ] Mobile RTL is reviewed independently when applicable.

## Accessibility

- [ ] Contrast and focus visibility are acceptable.
- [ ] Keyboard interaction remains usable.
- [ ] Form labels and accessible names are meaningful.
- [ ] Semantic document order is preserved.

## Engineering

- [ ] Existing application architecture is respected.
- [ ] No unnecessary dependency was introduced.
- [ ] Implementation remains maintainable.

## Visual Review

When a browser, preview, or screenshot capability is available:

- [ ] Inspect the actual rendered interface.
- [ ] Review representative screens and states.
- [ ] Review enabled themes and directions.
- [ ] Review desktop, tablet, and mobile layouts.
- [ ] Complete at least one refinement pass.

If rendered visual inspection is unavailable, state that clearly and complete code-based review.

## Redesign Comparison

For redesigns and audit+improve work, confirm improvement against the actual baseline in:

- clarity
- action discoverability
- hierarchy
- workflow efficiency
- scanability
- table/form efficiency
- responsive behavior
- RTL/LTR quality
- accessibility
- brand/palette coherence
- visual consistency
- maintainability

Do not use "looks newer" as evidence of improvement.
