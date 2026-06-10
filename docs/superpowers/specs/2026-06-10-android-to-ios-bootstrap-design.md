# Android-to-iOS Bootstrap Skill Design

## Goal

Add a new `android-to-ios-bootstrap` Skill that fills the gap between:

- `android-to-ios-porting`, which assumes there is already an iOS project and reusable iOS context
- `ios-development`, which assumes implementation can start inside an existing iOS codebase

The new Skill should help the user decide whether they need to:

1. initialize a brand-new iOS project
2. stabilize an existing but immature iOS project structure
3. move directly into `android-to-ios-porting` and then `ios-development`

## Problem

The current repository handles Android-to-iOS replication well only after the iOS side already exists.

Today:

- `android-to-ios-porting` expects `iOS 端现有架构和相似模块`
- `ios-development` expects an existing iOS architecture and supporting references

This leaves a workflow gap when:

- Android already has a stable feature
- iOS has not been created at all, or
- iOS exists but does not yet have a reliable structure for feature landing

In that state, the user currently has to manually infer which Skill to use first and how to bridge into the existing workflow.

## Proposed Skill

Create a new Skill:

```text
skills/android-to-ios-bootstrap/
├── SKILL.md
└── bootstrap-checklist.md
```

## Skill Responsibility

`android-to-ios-bootstrap` is a routing and initialization-decision Skill.

It should:

- inspect Android-side reality
- inspect iOS-side project status
- classify the current scenario
- output the recommended next-step workflow
- define the minimum iOS bootstrap structure when the iOS side is missing or structurally unstable

It should not:

- replace `android-to-ios-porting`
- replace `ios-development`
- directly own full iOS feature implementation
- pretend to know iOS project facts that are not visible in code or docs

## Supported Scenarios

The new Skill should explicitly support three scenarios:

### Scenario A: iOS project does not exist

The Skill should:

- recognize that there is no usable iOS codebase yet
- extract Android-side user-visible behavior and platform-neutral logic
- propose the minimum viable iOS project structure
- identify the first directories/files/modules that should be created
- recommend the next step as:
  - bootstrap the iOS project structure
  - then use `ios-development` for skeleton landing
  - then use `android-to-ios-porting` or continue with `ios-development` for feature implementation

### Scenario B: iOS project exists but structure is not ready

The Skill should:

- recognize that an iOS repository/app exists but is missing stable architecture or reusable module patterns
- describe the minimum architecture stabilization needed before feature replication
- identify what can be reused versus what must be introduced
- recommend the next step as:
  - stabilize structure first
  - then continue with `android-to-ios-porting`
  - then implement via `ios-development`

### Scenario C: iOS project exists and is ready

The Skill should:

- recognize that the current iOS project has enough structure to accept the feature
- skip bootstrap recommendations except for small notes
- route the user directly to:
  - `android-to-ios-porting`
  - then `ios-development`

## Inputs

The new Skill should require or prefer:

- Android implemented code
- product and interaction requirements
- known platform differences and constraints
- iOS project status:
  - no project
  - existing but immature
  - existing and stable
- if an iOS project exists:
  - directory structure
  - current architecture patterns
  - similar modules if available

## Workflow

`SKILL.md` should guide the agent through this sequence:

1. Read Android-side implemented code and identify user-visible behavior.
2. Extract platform-neutral logic:
   - flow
   - state model
   - API interactions
   - error handling
   - analytics/telemetry
3. Inspect current iOS-side status.
4. Classify the scenario into A / B / C.
5. If A or B:
   - propose the minimum viable iOS structure
   - identify initial module/file boundaries
   - define what must exist before actual feature replication starts
6. If C:
   - explain why direct replication is viable
7. Recommend the exact next Skill sequence.
8. Output validation approach, unverified items, and risks.

## Output Format

The Skill should produce a strongly structured output:

```text
【iOS 当前状态判断】
【Android 现有行为概览】
【平台无关逻辑】
【是否需要先创建或补齐 iOS 工程】
【推荐的 iOS 工程结构】
【首批应创建或修改的文件/模块】
【必须保持一致的行为】
【允许保留的平台差异】
【建议下一步 Skill】
【验证方式】
【未验证项】
【风险点】
```

## Supporting File

Add:

```text
skills/android-to-ios-bootstrap/bootstrap-checklist.md
```

This file should contain a practical checklist for the bootstrap decision, for example:

- whether iOS project exists
- whether there is a stable app/module structure
- whether state management conventions are visible
- whether networking, error handling, and navigation patterns exist
- whether there are comparable iOS screens/modules to reuse
- whether feature replication can begin immediately

`SKILL.md` must explicitly require reading and using this checklist.

## Integration with Existing Skills

The new Skill should integrate cleanly with current workflow:

- `context-bootstrap`
  - still used first when project context is unknown
- `android-to-ios-bootstrap`
  - used when Android exists and iOS project status is unclear or incomplete
- `android-to-ios-porting`
  - used once the iOS side is ready to receive replicated behavior
- `ios-development`
  - used when actual iOS implementation begins

## Routing Guidance to Add

The repository should eventually teach this route in its user-facing docs:

- If Android feature exists and iOS project is missing or unclear:
  - `context-bootstrap` → `android-to-ios-bootstrap`
- If bootstrap result says project must be created/stabilized:
  - `ios-development`
- Once structure is ready:
  - `android-to-ios-porting` → `ios-development`

## Constraints

The Skill must enforce:

- do not mechanically translate Android code
- behavior consistency is more important than structural mimicry
- do not fabricate iOS architectural facts
- unresolved project-state assumptions must be written to `未验证项`
- the Skill is for decision and bootstrap guidance, not full feature delivery

## Success Criteria

This Skill is successful if:

1. a user with no iOS project can get a clear bootstrap path
2. a user with a weak iOS project can get a stabilization path
3. a user with a ready iOS project is routed quickly to the existing replication workflow
4. the new Skill reduces ambiguity instead of adding another overlapping Skill
