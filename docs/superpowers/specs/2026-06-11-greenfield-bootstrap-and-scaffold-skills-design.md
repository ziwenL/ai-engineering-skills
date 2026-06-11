# Greenfield Bootstrap and Scaffold Skills Design

## Goal

Add a first-class workflow for creating brand-new client and server projects through this repository, instead of only supporting development inside already-existing codebases.

The first batch should cover:

- Android app creation
- iOS app creation
- backend service creation

The new design should follow a two-layer model:

1. a bootstrap routing layer that decides how a new project should be started
2. platform scaffold layers that create the minimum runnable project skeleton for each platform

This should let the repository support both:

- existing-project development workflows
- greenfield project creation workflows

without collapsing those responsibilities into the same Skills.

## Problem

The current repository is strong once a project already exists, but weak when the user wants to start from zero.

Today:

- `android-development` assumes an existing Android project and architecture references
- `ios-development` assumes an existing iOS project and reusable patterns
- `backend-development` assumes an existing backend service structure
- `technical-design` explains architecture but does not create project skeletons
- `context-bootstrap` builds context, but does not decide how a new multi-end project should be initialized

This leaves a workflow gap when the user wants to use this repository to:

- initialize a brand-new Android app
- initialize a brand-new iOS app
- initialize a brand-new backend service
- coordinate startup order across multiple ends

In that state, the user currently has to manually decide:

- which end should be started first
- what minimum project structure should exist
- which conventions should be shared across ends
- when to move from planning into actual project scaffolding

That manual gap is exactly where AI tends to generate unstable, over-scaffolded, or inconsistent output.

## Proposed Skills

Create four new Skills:

```text
skills/greenfield-bootstrap/
├── SKILL.md
└── bootstrap-checklist.md

skills/android-app-scaffold/
├── SKILL.md
├── scaffold-checklist.md
└── default-stack.md

skills/ios-app-scaffold/
├── SKILL.md
├── scaffold-checklist.md
└── default-stack.md

skills/backend-service-scaffold/
├── SKILL.md
├── scaffold-checklist.md
└── default-stack.md
```

## Design Principles

The new Skills should follow these principles:

1. Separate routing from implementation.
2. Prefer a recommended default stack, but allow explicit alternatives.
3. Create only the minimum runnable and extensible project shell.
4. Do not expand into full feature implementation during scaffolding.
5. Integrate cleanly with existing Skills instead of replacing them.

This means the new workflow is intentionally split:

- `greenfield-bootstrap` decides how to start
- scaffold Skills create platform project shells
- existing development Skills continue implementation afterward

## Skill Responsibilities

### `greenfield-bootstrap`

`greenfield-bootstrap` is the orchestration layer for brand-new project startup.

It should:

- determine whether the request is single-end or multi-end
- determine whether backend should start before the clients
- define shared naming, boundary, and startup constraints
- identify the first Skills that should run next
- output the startup sequence and validation path

It should not:

- deeply scaffold a platform-specific project
- replace `technical-design`
- replace `api-design`
- replace `android-app-scaffold`, `ios-app-scaffold`, or `backend-service-scaffold`
- generate a large amount of platform-specific implementation code

### `android-app-scaffold`

`android-app-scaffold` is the Android greenfield scaffold layer.

It should:

- recommend a default Android app stack
- allow one or more explicit fallback options
- define the minimum project/module structure
- create the first runnable shell
- define the first files, configuration, and verification path
- route follow-up implementation to `android-development`

It should not:

- own long-term feature implementation
- replace `technical-design`
- generate an overbuilt multi-module architecture by default
- front-load release or CI complexity unless explicitly required

### `ios-app-scaffold`

`ios-app-scaffold` is the iOS greenfield scaffold layer.

It should:

- recommend a default iOS app stack
- allow one or more explicit fallback options
- define the minimum project structure and layering
- create the first runnable shell
- define the first files, configuration, and verification path
- route follow-up implementation to `ios-development`

It should not:

- replace `android-to-ios-bootstrap`
- replace `ios-development`
- generate a complex multi-target or advanced package layout by default
- pretend that future cross-platform constraints are already validated

### `backend-service-scaffold`

`backend-service-scaffold` is the backend greenfield scaffold layer.

It should:

- recommend a default backend service stack
- allow one or more explicit fallback options
- define the minimum service structure
- create the first runnable API shell
- define configuration, health check, logging, error handling, and first tests
- route follow-up implementation to `backend-development`

It should not:

- replace `api-design`
- replace `backend-development`
- expand into full business logic
- front-load microservice decomposition or deployment complexity by default

## First-Batch Scope

The first batch should be intentionally narrow and reusable.

### In scope

- startup routing for Android + iOS + backend
- default startup sequence for multi-end projects
- recommended default stack plus alternatives
- minimum runnable project shell for each platform
- first directories/modules/files/configuration
- validation path
- explicit unverified items and risks

### Out of scope

- Web or admin frontend scaffolding
- monorepo-wide orchestration
- CI/CD generation
- release pipeline generation
- complex multi-target iOS setups
- aggressive Android modularization
- microservice platform decomposition
- infrastructure-as-code

## Supported Scenarios

The first version should explicitly support these scenarios.

### Scenario A: Backend-only greenfield service

The user wants to start only a backend service.

The workflow should be:

```text
context-bootstrap
→ greenfield-bootstrap
→ technical-design
→ api-design
→ backend-service-scaffold
→ backend-development
```

### Scenario B: Client-only greenfield app

The user wants to start only Android or only iOS.

The workflow should be:

```text
context-bootstrap
→ greenfield-bootstrap
→ technical-design
→ android-app-scaffold / ios-app-scaffold
→ android-development / ios-development
```

### Scenario C: Backend + client greenfield startup

The user wants to start a backend plus one or both mobile clients.

The default workflow should be:

```text
context-bootstrap
→ greenfield-bootstrap
→ technical-design
→ api-design
→ backend-service-scaffold
→ android-app-scaffold / ios-app-scaffold
→ backend-development
→ android-development / ios-development
```

The design should recommend backend-first scaffold by default when:

- login/authentication exists
- list/detail data depends on server response shape
- error-code and response conventions matter to client structure
- client behavior depends on stable API boundaries

It may recommend client-first only when:

- the first milestone is local-only demo validation
- the backend is intentionally mocked
- the client shell must be demonstrated before server delivery

## Inputs

### `greenfield-bootstrap`

Should require or prefer:

- product goal
- first milestone scope
- target ends:
  - Android
  - iOS
  - backend
- whether multiple ends must move in parallel
- whether login, payment, push, upload, local storage, analytics, or offline capability is needed
- known team preferences
- known delivery constraints
- whether API contracts or prototypes already exist
- `bootstrap-checklist.md`

### `android-app-scaffold`

Should require or prefer:

- Android target scope
- default stack preference or openness to recommendation
- whether multi-module setup is required now
- networking, login, storage, analytics, and routing needs
- whether the first milestone is app shell or a business home screen
- `scaffold-checklist.md`
- `default-stack.md`

### `ios-app-scaffold`

Should require or prefer:

- iOS target scope
- SwiftUI or UIKit preference if known
- whether modularization is required now
- networking, login, persistence, and analytics needs
- whether Android parity is a future requirement
- `scaffold-checklist.md`
- `default-stack.md`

### `backend-service-scaffold`

Should require or prefer:

- service type
- REST requirement
- auth requirement
- database expectation
- cache or queue expectation
- configuration and deployment environment expectations
- logging and monitoring baseline expectations
- `scaffold-checklist.md`
- `default-stack.md`

## Workflow

### `greenfield-bootstrap`

`SKILL.md` should guide the agent through this sequence:

1. Read current context and first-milestone goal.
2. Read `bootstrap-checklist.md`.
3. Determine whether the startup is:
   - backend only
   - Android only
   - iOS only
   - backend + Android
   - backend + iOS
   - backend + Android + iOS
4. Identify cross-end dependencies.
5. Recommend a default startup order.
6. Define shared constraints:
   - naming
   - API boundary ownership
   - DTO / model consistency expectations
   - environment/config conventions
7. Define what each end should do in phase 1 and what it must not do yet.
8. Recommend the exact next Skill sequence.
9. Output validation method, unverified items, and risks.

### `android-app-scaffold`

1. Read `scaffold-checklist.md` and `default-stack.md`.
2. Determine whether single-module or multi-module startup is justified.
3. Recommend the default stack and name alternatives if needed.
4. Define the minimum app structure:
   - app/module layout
   - UI shell
   - network placeholder
   - state/data boundary
5. Define the first files and configuration.
6. Create only the minimum runnable shell.
7. Route follow-up work to `android-development`.
8. Output validation method, unverified items, and risks.

### `ios-app-scaffold`

1. Read `scaffold-checklist.md` and `default-stack.md`.
2. Determine whether a minimal single-project structure is enough.
3. Recommend the default stack and name alternatives if needed.
4. Define the minimum app structure:
   - app shell
   - view/state/service boundaries
   - navigation placeholder
   - networking placeholder
5. Define the first files and configuration.
6. Create only the minimum runnable shell.
7. Route follow-up work to `ios-development`.
8. Output validation method, unverified items, and risks.

### `backend-service-scaffold`

1. Read `scaffold-checklist.md` and `default-stack.md`.
2. Determine whether the first version should be a single service shell.
3. Recommend the default stack and name alternatives if needed.
4. Define the minimum service structure:
   - config loading
   - health check
   - base routing
   - error handling
   - logging
   - first test boundary
5. Define the first files and configuration.
6. Create only the minimum runnable shell.
7. Route follow-up work to `backend-development`.
8. Output validation method, unverified items, and risks.

## Output Format

All four Skills should use a strongly aligned output structure.

```text
【当前启动判断】
【推荐默认方案】
【备选方案与取舍】
【首批应创建的目录/模块/文件】
【初始化步骤】
【本阶段不应提前做的事】
【下一步建议 Skill】
【验证方式】
【未验证项】
【风险点】
```

`greenfield-bootstrap` should additionally include:

```text
【推荐启动顺序】
【多端职责边界】
【共享命名与接口约束】
```

## Supporting Files

### `greenfield-bootstrap`

Add:

```text
skills/greenfield-bootstrap/bootstrap-checklist.md
```

This file should help the agent decide:

- which ends are included
- whether cross-end startup dependencies exist
- whether backend-first is needed
- whether the first milestone is demo-first or production-oriented
- whether there are missing constraints that must remain in `未验证项`

### Scaffold Skills

Each scaffold Skill should have:

```text
scaffold-checklist.md
default-stack.md
```

`scaffold-checklist.md` should focus on readiness and scope control.

`default-stack.md` should define:

- the recommended default stack
- one or more alternative stacks
- when to keep the default
- when to switch

Each `SKILL.md` must explicitly require reading and using these support files.

## Recommended Defaults

The first version should use a style of:

- recommended default stack
- explicit alternatives
- explicit switching conditions

This matches the intended repository philosophy:

- not hard-coded to only one stack forever
- not so abstract that the Skills become non-actionable

This spec intentionally fixes the default-selection pattern first, without prematurely binding every platform to a final concrete stack. Each scaffold Skill should follow this pattern:

1. recommend one default
2. expose one or two alternatives
3. explain why the default is preferred for the first batch
4. avoid deep branching unless real constraints require it

## Integration with Existing Skills

The new Skills should integrate with the current workflow like this:

- `context-bootstrap`
  - still runs first when project context is unknown
- `greenfield-bootstrap`
  - runs when the project does not yet exist or when the user explicitly wants to create a new project shell
- `technical-design`
  - still owns architecture decisions
- `api-design`
  - still owns API contract design
- `android-app-scaffold`
  - creates Android shell after design decisions are clear enough
- `ios-app-scaffold`
  - creates iOS shell after design decisions are clear enough
- `backend-service-scaffold`
  - creates backend shell after service/API direction is clear enough
- `android-development`
  - continues feature work after Android scaffold
- `ios-development`
  - continues feature work after iOS scaffold
- `backend-development`
  - continues feature work after backend scaffold

The new Skills should not change the role of:

- `android-to-ios-bootstrap`
- `android-to-ios-porting`

Those remain specialized for replication from an already-existing Android implementation.

## Routing Guidance to Add Later

The repository should eventually teach these user-facing routes:

### If the project does not exist yet

```text
context-bootstrap
→ greenfield-bootstrap
→ technical-design
→ scaffold skill(s)
→ development skill(s)
```

### If backend and mobile start together

```text
context-bootstrap
→ greenfield-bootstrap
→ technical-design
→ api-design
→ backend-service-scaffold
→ android-app-scaffold / ios-app-scaffold
```

### If Android already exists and iOS is missing

```text
context-bootstrap
→ android-to-ios-bootstrap
→ android-to-ios-porting
→ ios-development
```

This keeps greenfield startup and cross-platform replication as separate, non-overlapping workflows.

## Constraints

The new Skills must enforce:

- do not scaffold more than the first milestone needs
- do not skip startup sequencing decisions in multi-end projects
- do not turn design assumptions into fake facts
- unresolved product or stack assumptions must go into `未验证项`
- validation must be explicit even during scaffold work
- the purpose is to create stable project entry shells, not full applications or services

## Success Criteria

This design is successful if:

1. a user can create a brand-new Android, iOS, or backend project through this repository
2. a user can coordinate backend + mobile startup without manually inventing the order
3. scaffold output is actionable, minimal, and extensible
4. the new Skills complement rather than overlap with existing development Skills
5. the first batch is narrow enough to implement cleanly and expand later
