# Existing Product Audit and Improvement

Use this reference whenever the user asks to review, improve, modernize, clean up, fix, or redesign an existing interface.

The goal is to improve the product without destroying working workflows, introducing design drift, or turning a UI task into an uncontrolled rewrite.

## Existing-Product Modes

Choose one mode from the user's intent:

### 1. Audit Only

Use when the user asks to inspect, review, critique, or report issues.

Do not modify code.

Deliver:

- current-state summary
- issue list grouped by UX, visual design, responsive, accessibility, RTL/LTR, design-system, and implementation quality
- severity and impact
- evidence
- recommended remediation
- suggested implementation order

### 2. Audit and Improve

Use when the user asks to improve, fix, refine, modernize, or optimize the existing UI/UX.

Default workflow:

`Baseline -> Audit -> Prioritize -> Fix Safe Issues -> Validate -> Compare -> Refine`

Do not require a full redesign process for ordinary improvements.

### 3. Controlled Redesign

Use when existing structure materially prevents good UX or when the user explicitly requests a redesign.

Default workflow:

`Baseline -> Audit -> Redesign Scope -> Approve Direction -> Representative Screen -> Validate -> Roll Out -> Regression QA`

Use the normal approval gates for broad structural or visual-system changes.

## Step 1 — Establish the Baseline

Before changing code, inspect enough of the existing product to understand the system.

Determine where possible:

- application shell and navigation
- main user roles
- high-frequency workflows
- representative pages
- current component library
- reusable components
- existing tokens and CSS variables
- typography and fonts
- color/theme architecture
- responsive strategy
- RTL/LTR/localization behavior
- forms, tables, filters, dialogs, charts, alerts, and notifications
- loading, empty, error, success, partial-data, permission, and disabled states
- authentication/system pages
- accessibility patterns
- important business rules visible in the UI
- current tests and visual/regression tooling

If browser/preview access exists, inspect the rendered application before relying only on source code.

For large products, sample representative surfaces instead of reading every page before forming a useful baseline.

## Step 2 — Preserve Product Contracts

Treat the existing application as a working system.

Do not silently change:

- permissions
- role visibility
- business rules
- validation semantics
- API contracts
- data meaning
- destructive-action behavior
- authentication flows
- routing semantics
- keyboard behavior
- saved user preferences
- localization behavior

A visual improvement must not create a functional regression.

When a UX improvement appears to require a product-rule change, surface it separately and ask for approval.

## Step 3 — Build an Audit Matrix

Review the existing product across these dimensions.

### Product and Workflow

Check:

- screen purpose
- primary task
- action discoverability
- unnecessary steps
- repeated work
- confusing navigation
- poor grouping
- missing feedback
- error recovery
- destructive-action safety
- information overload
- missing context
- mismatch between UI structure and user mental model

### Information Architecture

Check:

- navigation hierarchy
- naming consistency
- page hierarchy
- breadcrumbs where useful
- tabs and sub-navigation
- content grouping
- settings organization
- duplicated or competing navigation

### Visual Hierarchy

Check:

- primary vs secondary emphasis
- typography scale
- spacing rhythm
- alignment
- density
- unnecessary containers
- card overuse
- excessive radius/shadows/gradients
- weak contrast between levels
- inconsistent action hierarchy
- oversized headers or sidebars

### Components and Design System

Check:

- duplicate components
- uncontrolled variants
- raw colors and spacing values
- inconsistent button/input/table behavior
- icon-family inconsistency
- missing semantic tokens
- theme drift
- inconsistent states
- obsolete components still in use

### Tables and Operational UI

Check:

- useful columns
- scanability
- sorting
- filtering
- search scope
- active-filter visibility
- pagination
- bulk actions
- row actions
- sticky behavior
- density
- horizontal overflow
- empty/loading/error states
- mobile strategy

### Forms

Check:

- field grouping
- visible labels
- validation clarity
- error placement
- save behavior
- unsaved changes
- disabled/loading state
- field order
- keyboard flow
- mobile layout
- technical fields in RTL interfaces

### Responsive Behavior

Check representative widths, not only breakpoints in code.

Review:

- navigation adaptation
- content priority
- table behavior
- filter behavior
- action placement
- dialogs/drawers
- forms
- charts
- overflow
- sticky elements
- touch targets
- mobile RTL/LTR independently when applicable

### Accessibility

Check:

- contrast
- keyboard navigation
- focus visibility
- semantic HTML
- accessible names
- label associations
- status conveyed beyond color
- dialog/menu focus management
- logical reading order
- reduced motion
- target size

### RTL / LTR and Localization

When applicable, check:

- document direction
- logical CSS properties
- mixed-direction strings
- table alignment/sticky columns
- pagination
- breadcrumbs
- drawers
- directional icons
- charts
- dates/digits
- mobile direction behavior

## Step 4 — Classify Findings

Every meaningful finding should have:

- `Severity`: Critical / High / Medium / Low
- `Impact`: task failure / error risk / slowdown / confusion / inconsistency / accessibility / visual quality / maintainability
- `Scope`: local / component / page / workflow / system
- `Confidence`: high / medium / low
- `Fix Type`: safe local fix / refactor / design-system change / workflow change / product decision

Do not assign severity based on visual dislike alone.

### Critical

Examples:

- user cannot complete a primary task
- destructive action is dangerously ambiguous
- permission or identity state is misleading
- severe accessibility blocker
- important content becomes inaccessible on common viewport sizes

### High

Examples:

- frequent workflow causes repeated confusion or errors
- navigation makes primary destinations hard to find
- table/form behavior materially slows common work
- severe RTL/LTR or responsive defect

### Medium

Examples:

- inconsistent hierarchy
- inefficient interaction
- component inconsistency
- weak empty/error state
- moderate accessibility issue

### Low

Examples:

- cosmetic inconsistency
- minor spacing/radius/icon polish
- low-impact visual cleanup

## Step 5 — Decide What Can Be Fixed Automatically

### Safe to fix without a new approval gate

When the user asked for improvement/fixing, normally proceed with well-supported, low-risk changes such as:

- spacing/alignment cleanup
- typography consistency
- contrast/focus improvements
- broken responsive behavior
- obvious RTL/LTR bugs
- inconsistent component states
- duplicate visual styles consolidated into existing patterns
- accessible labels/semantics
- table overflow and action-placement fixes
- loading/empty/error presentation improvements
- small visual hierarchy improvements
- removal of unjustified decoration that does not change workflow

Still preserve existing behavior.

### Require approval before broad propagation

Pause before:

- replacing the navigation model
- changing core information architecture
- changing primary workflows
- changing a global visual direction when no approved profile exists
- large-scale density change
- new design-system foundation
- changing brand identity
- changing business-visible terminology
- introducing a new UI framework
- major component-library migration
- changing authentication or permission UX semantics
- removing features or fields
- converting a multi-step workflow into a substantially different process

## Existing Project Without a Design Profile

Do not treat the absence of `design-profile.md` as a reason to block useful improvements.

First infer an `Observed Baseline` from the current product:

- existing visual style
- density
- typography
- palette
- surface treatment
- navigation
- themes
- direction
- responsive behavior
- recurring component patterns

Then decide:

### Local / corrective work

Use the Observed Baseline as a temporary constraint.

Fix defects and inconsistencies without forcing full discovery.

### Broad redesign or design-system change

Run Partial or Full Discovery as appropriate.

Recommend a new Design Profile and get approval before broad rollout.

If a coherent system emerges and the user approves it, create `design-profile.md`.

## Representative-Screen Strategy

For medium or large existing products, choose one or more representative surfaces before broad rollout.

Good candidates include:

- main dashboard/home
- primary operational table
- create/edit form
- record/detail page
- settings page
- mobile navigation state

Choose screens that exercise the shared components and difficult states.

## Before / After Comparison

For every meaningful redesign or improvement, compare the new result against the baseline.

Evaluate:

- task clarity
- action discoverability
- number of steps
- information hierarchy
- scanability
- table/form efficiency
- error prevention
- feedback quality
- responsive behavior
- RTL/LTR quality
- accessibility
- consistency
- maintainability

Do not claim improvement merely because the UI looks newer.

## Regression Review

After implementation, verify that the changes did not regress:

- routing
- permissions
- validation
- form submission
- keyboard use
- table interactions
- filters/search/sort
- destructive actions
- responsive layouts
- theme behavior
- localization
- loading/error handling
- existing tests

Run available tests, linters, type checks, and visual/regression tools when practical.

If a check cannot be run, state that explicitly.

## Deliverable for Audit + Improve

When the user asks for review and improvement, finish with a concise summary containing:

1. major problems found
2. high-impact changes made
3. behavior intentionally preserved
4. validation performed
5. remaining risks or items needing product approval

Do not overwhelm the user with every minor CSS edit.
