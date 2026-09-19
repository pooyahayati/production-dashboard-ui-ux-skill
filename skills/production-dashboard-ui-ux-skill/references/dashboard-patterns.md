# Dashboard and Product UI Patterns

## Dashboard philosophy

A dashboard should answer:

- what needs attention
- what changed
- what is abnormal
- what should happen next
- what can wait

Do not start with cards and charts. Start with user decisions.

## Shell and navigation

Use a stable shell appropriate to destination count, hierarchy, frequency, roles, and viewport.

Avoid:

- duplicate navigation
- excessive nesting
- icon-only critical destinations
- oversized sidebars
- decorative separators

Persian navigation normally originates from the right; English normally from the left.

## Page headers

Keep operational headers compact.

Communicate:

- location and context
- purpose
- primary action

Normally one action should be visually dominant.

## Metrics

Do not default to four KPI cards.

A prominent metric should be important, interpretable, and contextualized with time or comparison where useful.

## Tables

Treat tables as working tools.

Define:

- identifier
- operational columns
- status and numeric fields
- search scope
- filters
- sort
- pagination
- selection and bulk actions
- row actions
- column priority
- density
- sticky behavior
- responsive strategy

Do not expose every database field.

Keep frequent row actions discoverable; move rare actions to overflow.

Show active filters and a clear-filter action.

For large datasets read `performance.md`.

## Forms

Treat forms as workflows.

Use:

- meaningful grouping
- visible labels
- explicit save behavior
- clear validation
- preserved valid values after errors
- unsaved-change protection for meaningful work

Prefer one column for complex or long-label forms.

Use multiple columns only when relationships and available width justify it.

## Filters

Design around user decisions, not database schema.

On mobile, adapt to a drawer, bottom sheet, or dedicated view when appropriate.

## Charts

Before adding a chart answer:

`What question does this chart answer?`

Common mappings:

- trend -> line
- category comparison -> bar
- distribution -> histogram
- relationship -> scatter
- goal progress -> progress indicator
- single value -> metric

Avoid decorative or 3D charts and excessive series or colors.

Always clarify:

- unit
- time range and timezone where relevant
- missing or partial data
- comparison baseline

For accessibility:

- do not rely on color alone
- provide meaningful labels and summary
- provide a data/table alternative when exact values matter

Preserve chronological and analytical semantics in RTL rather than blindly mirroring.

## Status

Use a limited semantic palette:

- success
- warning
- danger
- info
- neutral

Do not use color alone.

Badges are for status or classification, not every ordinary value.

## Detail and CRM pages

Establish:

- identity
- status
- primary actions
- key properties
- related data
- activity and history
- secondary detail

Do not make every section an equal-weight card.

## Settings

Group by user mental model, not backend modules.

Separate high-impact operations.

Avoid nested tabs inside tabs.

## States

Differentiate:

- no data
- no search result
- no filtered result
- permission denied
- not configured
- missing connection
- load error
- partial data

Loading should preserve context.

Errors should explain:

- what happened
- what was affected
- what the user can do
- whether data was preserved

## High-impact actions

Use consequence text, confirmation, undo, or reversible removal based on risk.

Avoid confirmation fatigue.

## Authentication and system pages

Keep auth, 403, 404, 500, maintenance, offline, connection error, permission denied, and session expired inside the same design system.

Do not leave dead ends.

## Mobile

Do not automatically convert tables to cards.

Choose among:

- priority columns
- expandable rows
- summary and detail
- horizontal scroll
- dedicated detail view

Large dialogs may become full-screen views, sheets, or pages.

Keep primary actions discoverable.
