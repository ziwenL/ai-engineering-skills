# Compose Preview Conventions Skill Update Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add the approved Compose Preview conventions to the relevant Android skills and protect them with regression tests.

**Architecture:** Encode the convention at both execution points and default guidance points. `android-development` carries the implementation rule and checklist, `android-app-scaffold` carries the project-default guidance, and the Python skill-check tests guard the requirement from being removed later.

**Tech Stack:** Markdown skill docs, Python `unittest`, existing `scripts/check_skills.py` validation flow

---

### Task 1: Add a failing regression test

**Files:**
- Modify: `tests/test_check_skills.py`

- [ ] **Step 1: Add a test that expects Android skills to mention Compose Preview conventions**

- [ ] **Step 2: Run the targeted test file and confirm the new assertion fails before documentation changes**

- [ ] **Step 3: Keep the new test in place as the regression guard**

### Task 2: Update Android skill documentation

**Files:**
- Modify: `skills/android-development/SKILL.md`
- Modify: `skills/android-development/checklist.md`
- Modify: `skills/android-app-scaffold/SKILL.md`
- Modify: `skills/android-app-scaffold/default-stack.md`
- Modify: `skills/android-app-scaffold/scaffold-checklist.md`

- [ ] **Step 1: Add the Compose Preview conventions to the Android implementation skill workflow and constraints**

- [ ] **Step 2: Add explicit checklist coverage so the convention becomes part of self-review**

- [ ] **Step 3: Add scaffold-time guidance so new Compose projects inherit the convention from day one**

### Task 3: Verify and publish

**Files:**
- Verify: `tests/test_check_skills.py`
- Verify: `scripts/check_skills.py`

- [ ] **Step 1: Run the targeted Python tests and confirm they pass**

- [ ] **Step 2: Run the full skill checker and confirm the repository still validates**

- [ ] **Step 3: Commit the verified changes and push the current branch**
