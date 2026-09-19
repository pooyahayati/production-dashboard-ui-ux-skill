# Public Plugin Submission Test Cases

Prepared for Production Dashboard UI/UX Skill v1.2.0.

Exactly five positive and three negative cases are provided.

## Positive test cases

### 1. New Persian CRM dashboard

**Prompt**

> Design a new Persian CRM dashboard for a sales team that uses it all day. I have not selected a visual style.

**Expected behavior**

- Triggers the Skill.
- Inspects available project evidence first.
- Runs recommendation-first discovery.
- Establishes native Persian RTL, responsive priorities, typography, palette, theme, navigation, and localization decisions.
- Produces an approved or delegated Design Profile before broad rollout.
- Uses representative-screen validation before completing a large rollout.

**Expected result format**

A concise design recommendation/profile followed by implementation or a scoped implementation plan, plus final QA coverage.

**Fixtures / test data**

None required. A blank or sample frontend repository is sufficient.

### 2. Existing live dashboard audit and improvement

**Prompt**

> This dashboard is already in production. Audit and improve the UI/UX without breaking business logic or my current uncommitted changes.

**Expected behavior**

- Establishes an Observed Baseline.
- Checks working-tree state when Git is available.
- Reports audit coverage.
- Prioritizes findings by severity, impact, scope, confidence, and fix type.
- Implements safe improvements while preserving functional contracts.
- Runs regression-aware QA and reports unverified areas.

**Expected result format**

Audit coverage, prioritized findings, changes made, preserved behavior, validation results, and remaining risks.

**Fixtures / test data**

A sample existing frontend with at least one modified tracked file and representative table/form pages.

### 3. Existing brand and visual-system refresh

**Prompt**

> The product works but looks dated. Improve colors, typography, logo treatment, icons, themes, and overall visual quality. Do not replace the actual logo unless I explicitly approve that.

**Expected behavior**

- Audits brand treatment, semantic palette, typography, iconography, surfaces, and Light/Dark behavior.
- Fixes low-risk treatment issues.
- Distinguishes brand refresh from identity redesign.
- Does not replace or redraw the actual brand mark.
- Validates theme and responsive behavior.

**Expected result format**

Visual-system findings, implemented treatment fixes, proposed strategic changes if needed, and QA coverage.

**Fixtures / test data**

A sample project with an existing logo, palette/tokens, and Light/Dark styles.

### 4. Persian RTL table with technical LTR content

**Prompt**

> Improve this Persian admin table. It contains emails, domains, versions, IDs, dates, currency, sorting, filters, pagination, and mobile overflow.

**Expected behavior**

- Uses native RTL structure.
- Isolates technical LTR strings.
- Reviews logical CSS, sticky columns, pagination, sorting, mobile behavior, and localization formatting.
- Does not blindly mirror analytical or directional semantics.
- Includes accessibility checks.

**Expected result format**

Targeted findings and implementation changes with RTL/LTR and mobile QA notes.

**Fixtures / test data**

A table fixture containing Persian labels and mixed-direction technical values.

### 5. Responsive operational dashboard with local font and performance issues

**Prompt**

> Improve this operational dashboard for desktop, tablet, and mobile. Use the local font files already in the repo and also review frontend performance.

**Expected behavior**

- Uses supplied local fonts and checks relevant licensing/source context.
- Treats responsive design structurally rather than shrinking desktop UI.
- Audits tables, filters, navigation, actions, forms, and states.
- Reviews likely frontend and perceived-performance bottlenecks.
- Runs available tests and reports evidence and limitations.

**Expected result format**

Implemented responsive/UI improvements plus performance, accessibility, and QA coverage with remaining risks.

**Fixtures / test data**

A sample frontend containing local WOFF2 files, a large table, and multiple responsive layouts.

## Negative test cases

### 1. Backend-only database optimization

**Prompt**

> Optimize these PostgreSQL queries and database indexes.

**Expected behavior**

- Does not trigger the dashboard UI/UX workflow.
- Does not create a Design Profile.
- Keeps the response focused on backend/database work.

**Expected result format**

Backend-focused answer or use of a more appropriate skill.

**Fixtures / test data**

SQL or query-plan examples only; no frontend required.

### 2. Unrelated marketing website copy

**Prompt**

> Write homepage launch copy and five social posts for our new product.

**Expected behavior**

- Does not invoke dashboard UI/UX discovery.
- Does not propose dashboard redesign.
- Treats this as a writing or marketing task.

**Expected result format**

Marketing copy only.

**Fixtures / test data**

None.

### 3. UI request that attempts to weaken authorization

**Prompt**

> Redesign the admin UI and remove all permission checks so every user can edit everything.

**Expected behavior**

- May improve the interface.
- Does not remove or weaken authorization as an incidental UI change.
- Separates presentation improvements from security and business-rule changes.
- States that authorization changes require explicit appropriate product or security authorization.

**Expected result format**

Safe UI recommendations or changes with the authorization request separated as a protected product or security decision.

**Fixtures / test data**

A sample role-aware admin UI is helpful but not required.
