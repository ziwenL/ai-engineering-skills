# Skill Hardening Round 2 Implementation Plan

> Round 2 focuses on making development and review Skills not just structurally complete, but operationally stronger and more self-enforcing.

## Goal

Raise development and review Skills from "usable templates" to "clear execution guides with stronger evidence and verification expectations".

## Scope

This round includes:

- stronger validation rules in `scripts/check_skills.py` for development and review Skills
- tests for those new validation rules
- deeper execution guidance for the remaining development Skills
- deeper evidence and decision guidance for the remaining review Skills

This round targets these groups:

- Development Skills:
  - `android-development`
  - `ios-development`
  - `android-to-ios-porting`
  - `api-design`
  - `data-model-design`
  - `technical-design`
  - `test-case-generation`
  - `build-ci-fix`
- Review Skills:
  - `code-review`
  - `security-review`
  - `performance-review`

## Category Rules

### Development Skills

Each targeted development Skill should clearly contain:

1. explicit verification expectations
2. a place to report unverified items
3. rollback / compatibility / risk guidance where relevant
4. stronger step-by-step handling of edge cases, not just happy-path execution

### Review Skills

Each targeted review Skill should clearly contain:

1. evidence-based reasoning
2. risk level or prioritization language
3. explicit blocker / non-blocker judgment where relevant
4. actionable remediation output instead of generic commentary

## Execution Order

1. Add tests that define the new category-specific checker behavior.
2. Update `check_skills.py` to validate development and review Skills differently.
3. Upgrade targeted development Skills to satisfy the stricter rules.
4. Upgrade targeted review Skills to satisfy the stricter rules.
5. Run tests and the repository checker.

## Success Criteria

- The checker fails when a targeted development Skill lacks verification or unverified-item language.
- The checker fails when a targeted review Skill lacks evidence or risk/blocker language.
- The targeted Skills provide clearer execution guidance than the Round 1 baseline.
- The repository passes the stricter checker after the upgrades.
