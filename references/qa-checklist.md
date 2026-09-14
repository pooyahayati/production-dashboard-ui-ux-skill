# Final QA Checklist

Use before declaring a major UI task complete.

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

- [ ] Logo and favicon integration are correct.
- [ ] Relevant logo variants work across enabled themes.
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

For redesigns, confirm improvement in clarity, discoverability, hierarchy, workflow efficiency, responsive behavior, RTL/LTR quality, and maintainability.
