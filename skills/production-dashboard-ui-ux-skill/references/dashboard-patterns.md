# Dashboard and Product UI Patterns

## Dashboard Philosophy

A dashboard must answer:

- What needs attention?
- What changed?
- What is abnormal?
- What should the user do next?
- What can wait?

It is not a collection of cards and charts.

## Application Shell

Use a stable shell where appropriate:

- primary navigation
- top bar
- page header
- primary content
- optional context panel
- global feedback layer

Do not duplicate the same navigation in multiple places without purpose.

## Sidebar

Prioritize clear labels, grouping, active state, and role-aware visibility.

Avoid excessive nesting, huge logos, too many separators, overly wide sidebars, and critical icon-only navigation.

Persian sidebars normally start on the right; English sidebars normally start on the left.

## Page Header

Normally communicate:

- where the user is
- what the page is for
- the primary action

Keep operational headers compact.

Normally use one visually dominant primary action.

## Metrics

Do not default to four KPI cards.

A prominent metric should be important and interpretable.

Include comparison period when showing trend.

Prefer a few high-value metrics over many equal-priority KPIs.

## Tables

Before implementation define:

- primary identifier
- operational columns
- status/numeric fields
- search
- filters
- sort
- pagination
- selection
- bulk actions
- row actions
- column priority
- density
- responsive strategy
- sticky behavior

Do not expose every database field.

Frequently used row actions may remain visible; move rare actions to overflow.

Show selection count with bulk actions.

Show active filters and a clear-filter action.

Search copy should describe scope.

Use infinite scroll cautiously; deterministic admin workflows often benefit from pagination.

## Forms

Treat forms as workflows.

Group related fields.

Prefer one column when labels are long, validation is complex, or focus matters.

Use two columns only when fields are short and strongly related.

Avoid ordinary three/four-column data entry.

Labels must remain visible.

Define save behavior explicitly.

Preserve valid values after validation errors.

Consider unsaved-change protection for meaningful work.

## Filters

Design filters around real user decisions.

Common types:

- status
- date range
- owner
- category
- tag
- role
- priority
- location
- source

Do not create filters simply because a database field exists.

On mobile, use a drawer, bottom sheet, or dedicated filter view when appropriate.

## Charts

Before adding a chart, answer:

`What question does this chart answer?`

Mappings:

- trend -> line
- category comparison -> bar
- distribution -> histogram
- relationship -> scatter
- goal progress -> progress indicator
- single value -> metric

Use pie/donut sparingly.

Avoid decorative charts, 3D, excessive legends, and too many colors.

Preserve chronology and analytical semantics in RTL.

## Status

Use a limited semantic palette:

- success
- warning
- danger
- info
- neutral

Never rely on color alone.

Use badges for status/classification, not every ordinary value.

## CRM / Detail Pages

Establish record identity first.

Typical structure:

- identity
- status
- primary actions
- key properties
- related data
- activity/history
- secondary details

Activity timelines should show what happened, who, when, and related object.

Do not make every section an equal-weight card.

## Settings

Group settings by user mental model, not backend architecture.

Examples:

- General
- Account
- Users
- Permissions
- Notifications
- Integrations
- Billing
- Security
- Localization
- Advanced

Separate high-impact operations.

Avoid nested tabs inside tabs where possible.

## Empty States

Differentiate:

- no data
- no search result
- no filtered result
- no permission
- not configured
- missing connection
- load error

A useful empty state explains what is empty and what the user can do next.

## Loading

Preserve context.

Use local loading for local operations.

Choose skeleton, spinner, progress, optimistic update, or background status based on the task.

Do not block the whole page for a small update.

## Errors

Communicate:

- what happened
- what was affected
- what the user can do
- whether data was preserved

Avoid generic error copy when better context exists.

## High-Impact Actions

Protect high-impact actions appropriately.

Consider:

- clear consequence text
- confirmation
- undo
- reversible removal

Avoid confirmation fatigue.

## Authentication

Apply the same brand, typography, palette, themes, radius, icons, RTL/LTR, and responsive rules to applicable authentication pages.

Login should prioritize clear authentication, useful errors, credential visibility control, autofill compatibility, keyboard use, accessibility, and responsive behavior.

## System Pages

Style applicable:

- 403
- 404
- 500
- Maintenance
- Offline
- Connection Error
- Permission Denied
- Session Expired

Do not leave users at dead ends.

## Mobile

Do not automatically convert every table to cards.

Possible strategies:

- priority columns
- expandable rows
- summary + detail
- horizontal scroll
- dedicated detail view

Choose based on the task.

Large dialogs may become full-screen views, bottom sheets, or dedicated pages.

Keep primary actions discoverable.
