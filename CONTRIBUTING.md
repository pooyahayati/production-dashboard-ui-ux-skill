# Contributing

Contributions to **Production Dashboard UI/UX Skill** are welcome.

## Good contribution areas

- Real production dashboard UX patterns
- Persian RTL edge cases
- Bilingual RTL/LTR architecture
- Accessibility improvements
- Responsive dashboard behavior
- Data table and filtering workflows
- Design-system consistency
- Light/Dark theme edge cases
- Local typography and Persian/Latin pairing
- Removal of generic AI-generated UI patterns

## Contribution principles

Changes should improve agent decisions without making the skill unnecessarily rigid.

Prefer:

- reusable principles over one-off fixes
- product outcomes over visual trends
- concise core instructions
- conditional detail in `references/`
- preserving existing architecture and user intent
- observable QA criteria

Avoid:

- adding a rule for every isolated example
- turning one design preference into a universal requirement
- duplicating the same instruction across multiple files
- large generic UI tutorials that Codex already knows
- framework-specific requirements unless genuinely necessary

## Pull requests

A pull request should explain:

1. the problem or failure mode
2. the proposed change
3. why it belongs in the core skill or a specific reference
4. any UX, RTL/LTR, accessibility, or compatibility implications

Keep unrelated changes separate.
