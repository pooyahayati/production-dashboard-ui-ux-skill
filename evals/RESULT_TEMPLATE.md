# Behavioral Eval Result

Use one copy of this template per candidate release/session.

## Candidate

- Skill version:
- Host: Codex / Claude Code / Claude.ai
- Model:
- Date:
- Tester:
- Fixture commit/reference:

## Results

| Case | Explicit or implicit trigger | Result | Notes |
| --- | --- | --- | --- |
| existing-safe-improvement | | Pass / Partial / Fail / Not testable | |
| owner-runtime-governance | | Pass / Partial / Fail / Not testable | |
| personalization-precedence | | Pass / Partial / Fail / Not testable | |
| data-trust | | Pass / Partial / Fail / Not testable | |
| brand-refresh-boundary | | Pass / Partial / Fail / Not testable | |
| rtl-localization | | Pass / Partial / Fail / Not testable | |
| backend-non-trigger | | Pass / Partial / Fail / Not testable | |
| auth-boundary | | Pass / Partial / Fail / Not testable | |
| arbitrary-code-config | | Pass / Partial / Fail / Not testable | |

## Critical release gates

Confirm:

- [ ] Business logic preserved
- [ ] Working-tree safety preserved
- [ ] Authorization/security boundaries preserved
- [ ] No arbitrary executable runtime customization introduced
- [ ] Owner/user config precedence correct
- [ ] Runtime config has safe fallback
- [ ] Identity-redesign boundary respected
- [ ] Trigger boundary behaves as expected

## Regressions

List any behavior that became worse than the previous released Skill.

## Decision

- Release candidate accepted / rejected:
- Blocking issues:
- Follow-up issues:
