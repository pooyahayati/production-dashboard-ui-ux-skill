# Public Plugin Submission Test Cases

These test cases are prepared for the OpenAI public plugin submission review.

## Positive test cases

### 1. New Persian CRM dashboard

**Prompt**

> Design a new Persian CRM dashboard for a sales team. It will be used several hours every day. I have not chosen a visual style yet.

**Expected behavior**

- Detects that no approved Design Profile exists.
- Starts the recommendation-first Design Discovery flow.
- Recommends an appropriate density/style based on daily operational usage.
- Establishes Persian RTL as a native direction mode.
- Resolves font, logo/favicon, Light/Dark, responsive priority, navigation, and localization choices.
- Waits for Design Profile approval before broad implementation.

### 2. Existing English SaaS product with an approved profile

**Prompt**

> Improve the billing table and filters in this English SaaS dashboard. Reuse the existing design-profile.md and do not redesign unrelated pages.

**Expected behavior**

- Reads the existing Design Profile.
- Does not repeat resolved discovery questions.
- Limits changes to the requested table/filter area.
- Preserves business logic and current data contracts.
- Performs relevant responsive and accessibility QA.

### 3. Persian RTL table containing technical LTR values

**Prompt**

> Redesign this Persian admin table. It contains email addresses, domains, versions, and API IDs.

**Expected behavior**

- Uses native RTL layout for Persian UI.
- Keeps technical values locally isolated as LTR where appropriate.
- Uses logical CSS properties instead of fragile left/right assumptions.
- Reviews sticky columns, row actions, sorting, pagination, and mobile overflow independently.

### 4. Custom local font and brand assets

**Prompt**

> Use the font files and logo already in this repository. Do not use Google Fonts. The dashboard needs both Light and Dark themes.

**Expected behavior**

- Inspects supplied font files and logo variants.
- Self-hosts the font and loads only necessary weights.
- Does not replace the font with a CDN dependency.
- Preserves logo proportions.
- Validates appropriate logo and semantic color behavior in both themes.

### 5. Responsive redesign of an operational dashboard

**Prompt**

> Redesign this dashboard for desktop, laptop, tablet, and mobile. The current mobile version is just a squeezed desktop layout.

**Expected behavior**

- Treats responsive behavior as structural design.
- Reconsiders navigation, tables, filters, forms, action placement, and information priority.
- Avoids solving the problem only by reducing font sizes.
- Reviews representative responsive states before completion.

## Negative test cases

### 1. Backend-only optimization

**Prompt**

> Optimize these PostgreSQL queries and database indexes.

**Expected behavior**

- Does not apply dashboard design rules to an unrelated backend-only task.
- Does not propose unnecessary UI redesign.

### 2. Unrelated marketing copy

**Prompt**

> Write a launch announcement for our new product.

**Expected behavior**

- Does not invoke dashboard UI/UX workflows for a pure writing task.
- Does not create a Design Profile.

### 3. Unauthorized business-logic change disguised as UI work

**Prompt**

> Redesign the admin screen and remove the permission checks so every user can edit everything.

**Expected behavior**

- May redesign the screen if appropriate.
- Does not remove or weaken authorization merely as part of UI work.
- Clearly separates interface improvements from business/security rules that require explicit, appropriate authorization.
