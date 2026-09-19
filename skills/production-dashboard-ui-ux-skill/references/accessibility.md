# Accessibility

Target WCAG 2.2 AA where practical for production interfaces.

Automated checks help but do not replace manual interaction testing.

## Structure

Check:
- semantic landmarks
- heading hierarchy
- labels and accessible names
- table semantics
- form associations
- button/link semantics
- live regions only where useful
- DOM order matching meaningful reading order

Do not repair visual RTL/LTR ordering by breaking semantic order.

## Keyboard and focus

Verify:
- all interactive controls are keyboard reachable
- focus is visible
- tab order is logical
- dialogs trap and restore focus correctly
- menus and composite widgets follow expected keyboard behavior
- no keyboard traps
- skip/navigation mechanisms where appropriate

## Visual access

Verify:
- text and UI contrast
- status is not color-only
- focus indication
- zoom and reflow behavior
- readable typography
- sufficient target size
- reduced-motion preferences
- errors are visually and programmatically associated with fields

## Forms and validation

Provide:
- visible labels
- understandable instructions
- specific validation messages
- preserved valid values after errors
- summary/focus strategy for complex forms
- programmatic required/invalid states

## Dynamic UI

For loading, errors, toasts, live updates, and background jobs:
- announce important state changes when needed
- avoid excessive live-region noise
- preserve focus unless moving it is necessary
- provide non-visual state information

## Charts and data visualization

Charts should:
- not rely on color alone
- use readable labels and legends
- expose a meaningful text summary
- provide an accessible data alternative when exact values matter
- keep units, time ranges, and axes understandable

## Automated checks

When supported, use tools such as:
- axe or axe-core
- Playwright accessibility integrations
- framework linters
- Lighthouse accessibility checks

Treat automated results as evidence, not proof of full conformance.

## Manual checks

For representative workflows, test:
- keyboard-only use
- visible focus
- zoom and reflow
- screen-reader-friendly names/structure where tooling is available
- Light/Dark contrast
- RTL/LTR semantic order where relevant

Report what was actually tested.
