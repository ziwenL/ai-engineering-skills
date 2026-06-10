# Skill Hardening Round 1 Implementation Plan

> For this round, focus on building a reusable foundation: a clearer Skill standard, stronger automated checks, and three representative upgraded Skills.

## Goal

Raise the repository from "Skill skeletons exist" to "new and updated Skills have a consistent executable shape".

## Scope

This round includes:

- a stronger documented Skill standard
- automated validation in `scripts/check_skills.py`
- tests for the validation behavior
- upgraded `backend-development`, `frontend-development`, and `security-review`
- aligned authoring prompts so future Skill changes follow the same standard

This round does not yet include:

- rewriting every Skill in the repository
- updating adapter templates or the README to teach the new standard
- adding CI integration beyond a local checker and test command

## Target Standard

Each first-class `SKILL.md` should contain:

1. frontmatter: `name`, `description`
2. `## 适用场景`
3. `## 输入`
4. `## 工作流程`
5. `## 输出格式`
6. `## 约束`
7. `## 不适用场景`

If a Skill directory contains supporting files such as checklists or references, the main `SKILL.md` should explicitly tell the agent to read and use them.

## Execution Order

1. Add tests that describe the expected `check_skills.py` validation behavior.
2. Update `check_skills.py` to fail on missing required sections and unreferenced support files.
3. Refresh the writing guide and authoring prompts so new Skills target the same structure.
4. Upgrade three representative Skills to satisfy the new standard and reference their support files where relevant.
5. Run the new tests and the checker against the repository.

## Success Criteria

- `scripts/check_skills.py` detects structure problems instead of only missing files.
- The new tests pass locally.
- The three upgraded Skills are materially more executable than their prior versions.
- The repository itself passes the stricter checker after the selected changes.
