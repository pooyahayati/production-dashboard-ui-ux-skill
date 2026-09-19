# Final QA Checklist

Use before declaring major UI work complete.

## Coverage report

Record what was actually checked:

| Dimension | Coverage |
| --- | --- |
| Routes/screens | list |
| Workflows | list |
| Viewports | desktop/tablet/mobile/etc |
| Themes | Light/Dark |
| Direction | RTL/LTR |
| Roles | list or not tested |
| States | default/loading/empty/error/etc |
| Rendered inspection | yes/no |
| Automated checks | list |
| Not checked | list |

Do not imply coverage that was not performed.

## Existing-product regression

- baseline inspected
- working tree and user changes protected
- business logic preserved
- permissions preserved
- validation and data meaning preserved
- routing and deep links preserved
- before/after comparison performed where meaningful

## Product and UX

- screen purpose is clear
- primary action is discoverable
- hierarchy matches importance
- unnecessary steps and controls reduced
- empty, error, and permission states are useful
- destructive actions communicate consequence

## Design system

- semantic tokens used
- component states consistent
- uncontrolled variants reduced
- icon family coherent
- spacing, radius, and elevation intentional
- no unjustified AI-dashboard clichés

## Brand and typography

- logo treatment audited
- correct variants used
- palette semantics and contrast improved
- typography works at real sizes
- local fonts load correctly
- strategic identity changes were authorized
- third-party asset licensing checked when relevant

## Theme

For each supported theme:

- surface hierarchy
- text and border contrast
- status colors
- focus, hover, selected, and disabled
- forms, tables, and charts
- overlays, tooltips, and dialogs
- logo variant

## Responsive

At representative widths:

- navigation
- primary actions
- tables
- filters
- forms
- dialogs
- charts
- sticky regions
- overflow
- touch targets

## RTL/LTR and localization

Where applicable:

- document lang and dir
- logical CSS
- mixed-direction isolation
- table, pagination, and breadcrumb behavior
- directional icons
- chart semantics
- dates, numbers, currency, and timezone
- text expansion and truncation
- mobile direction

## Accessibility

Read `accessibility.md`.

Record automated and manual checks separately.

## Performance

Read `performance.md` when relevant.

Record measurements or inspection evidence rather than unsupported claims.

## Engineering

Run available:

- unit and integration tests
- lint
- type check
- build
- visual or regression tests
- accessibility tooling
- performance tooling where relevant

Do not hide failures.

## Visual review

When browser, preview, or screenshot tools are available:

1. render representative pages
2. inspect real content
3. inspect themes, directions, viewports, and states
4. fix issues
5. inspect again

If rendered QA is unavailable, say so.

## Final comparison

For redesigns compare baseline vs result on:

- task clarity
- discoverability
- steps
- hierarchy
- scanability
- form and table efficiency
- error prevention
- feedback
- responsiveness
- RTL/LTR
- accessibility
- performance where relevant
- brand coherence
- maintainability

"Looks newer" is not a success criterion.
