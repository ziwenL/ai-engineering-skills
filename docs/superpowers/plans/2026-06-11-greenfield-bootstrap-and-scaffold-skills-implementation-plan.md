# Greenfield Bootstrap and Scaffold Skills Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a greenfield startup layer to the repository by introducing `greenfield-bootstrap`, `android-app-scaffold`, `ios-app-scaffold`, and `backend-service-scaffold`, then wire them into validation and entry documentation.

**Architecture:** Implement the new workflow in two layers. First, extend repository validation so the new Skills are treated as first-class development Skills with support-file enforcement. Then add one routing Skill plus three scaffold Skills, each with explicit support files and aligned output structure, and finally route them through README and adapter templates so they are discoverable.

**Tech Stack:** Markdown Skills, Python validation script, Python `unittest`, repository docs/templates

---

## File Map

- Create: `skills/greenfield-bootstrap/SKILL.md`
- Create: `skills/greenfield-bootstrap/bootstrap-checklist.md`
- Create: `skills/android-app-scaffold/SKILL.md`
- Create: `skills/android-app-scaffold/scaffold-checklist.md`
- Create: `skills/android-app-scaffold/default-stack.md`
- Create: `skills/ios-app-scaffold/SKILL.md`
- Create: `skills/ios-app-scaffold/scaffold-checklist.md`
- Create: `skills/ios-app-scaffold/default-stack.md`
- Create: `skills/backend-service-scaffold/SKILL.md`
- Create: `skills/backend-service-scaffold/scaffold-checklist.md`
- Create: `skills/backend-service-scaffold/default-stack.md`
- Create: `docs/superpowers/plans/2026-06-11-greenfield-bootstrap-and-scaffold-skills-implementation-plan.md`
- Modify: `scripts/check_skills.py`
- Modify: `tests/test_check_skills.py`
- Modify: `README.md`
- Modify: `docs/getting-started.md`
- Modify: `docs/roadmap.md`
- Modify: `adapters/claude/CLAUDE.md.template`
- Modify: `adapters/codex/AGENTS.md.template`
- Modify: `adapters/cursor/cursor-rules.template.md`
- Modify: `adapters/generic/AI_AGENT.md.template`

## Task 1: Extend Skill Validation Coverage

**Files:**
- Modify: `scripts/check_skills.py`
- Modify: `tests/test_check_skills.py`

- [ ] **Step 1: Write failing tests for the new Skill categories**

Add these test methods to `tests/test_check_skills.py` inside `CheckSkillsScriptTest`:

```python
    def test_passes_for_greenfield_bootstrap_with_referenced_checklist(self) -> None:
        write_text(
            self.temp_dir / "skills" / "greenfield-bootstrap" / "SKILL.md",
            """
            ---
            name: greenfield-bootstrap
            description: 示例
            ---

            # Greenfield Bootstrap Skill

            ## 适用场景
            - 从 0 创建新项目

            ## 输入
            - 已确认目标
            - `bootstrap-checklist.md`

            ## 工作流程
            1. 读取 `bootstrap-checklist.md`
            2. 判断启动顺序

            ## 输出格式
            ```text
            【推荐启动顺序】
            【验证方式】
            【未验证项】
            ```

            ## 约束
            - 不直接展开完整实现

            ## 不适用场景
            - 已有稳定项目继续开发
            """,
        )
        write_text(
            self.temp_dir / "skills" / "greenfield-bootstrap" / "bootstrap-checklist.md",
            """
            # Bootstrap Checklist
            - [ ] 是否需要多端联动启动
            """,
        )

        result = self.run_check()

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("[OK] greenfield-bootstrap", result.stdout)

    def test_passes_for_android_app_scaffold_with_referenced_support_files(self) -> None:
        write_text(
            self.temp_dir / "skills" / "android-app-scaffold" / "SKILL.md",
            """
            ---
            name: android-app-scaffold
            description: 示例
            ---

            # Android App Scaffold Skill

            ## 适用场景
            - 创建 Android 新项目骨架

            ## 输入
            - 已确认目标
            - `scaffold-checklist.md`
            - `default-stack.md`

            ## 工作流程
            1. 读取 `scaffold-checklist.md`
            2. 读取 `default-stack.md`
            3. 生成最小骨架

            ## 输出格式
            ```text
            【推荐默认方案】
            【验证方式】
            【未验证项】
            ```

            ## 约束
            - 只创建最小可运行骨架

            ## 不适用场景
            - 已有稳定 Android 项目继续开发
            """,
        )
        write_text(
            self.temp_dir / "skills" / "android-app-scaffold" / "scaffold-checklist.md",
            """
            # Scaffold Checklist
            - [ ] 是否确实需要多模块
            """,
        )
        write_text(
            self.temp_dir / "skills" / "android-app-scaffold" / "default-stack.md",
            """
            # Default Stack
            - 默认：Jetpack Compose
            """,
        )

        result = self.run_check()

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("[OK] android-app-scaffold", result.stdout)

    def test_fails_when_greenfield_bootstrap_checklist_is_not_referenced(self) -> None:
        write_text(
            self.temp_dir / "skills" / "greenfield-bootstrap" / "SKILL.md",
            """
            ---
            name: greenfield-bootstrap
            description: 示例
            ---

            # Greenfield Bootstrap Skill

            ## 适用场景
            - 从 0 创建新项目

            ## 输入
            - 已确认目标

            ## 工作流程
            1. 判断启动顺序

            ## 输出格式
            ```text
            【推荐启动顺序】
            【验证方式】
            【未验证项】
            ```

            ## 约束
            - 不直接展开完整实现

            ## 不适用场景
            - 已有稳定项目继续开发
            """,
        )
        write_text(
            self.temp_dir / "skills" / "greenfield-bootstrap" / "bootstrap-checklist.md",
            """
            # Bootstrap Checklist
            - [ ] 是否需要多端联动启动
            """,
        )

        result = self.run_check()

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("未引用的辅助文件", result.stdout)
        self.assertIn("bootstrap-checklist.md", result.stdout)

    def test_fails_when_backend_service_scaffold_lacks_unverified_item_language(self) -> None:
        write_text(
            self.temp_dir / "skills" / "backend-service-scaffold" / "SKILL.md",
            """
            ---
            name: backend-service-scaffold
            description: 示例
            ---

            # Backend Service Scaffold Skill

            ## 适用场景
            - 创建服务端骨架

            ## 输入
            - 已确认目标
            - `scaffold-checklist.md`
            - `default-stack.md`

            ## 工作流程
            1. 读取 `scaffold-checklist.md`
            2. 读取 `default-stack.md`

            ## 输出格式
            ```text
            【推荐默认方案】
            【初始化步骤】
            ```

            ## 约束
            - 只创建最小可运行骨架

            ## 不适用场景
            - 已有稳定服务继续开发
            """,
        )
        write_text(
            self.temp_dir / "skills" / "backend-service-scaffold" / "scaffold-checklist.md",
            """
            # Scaffold Checklist
            - [ ] 是否需要数据库
            """,
        )
        write_text(
            self.temp_dir / "skills" / "backend-service-scaffold" / "default-stack.md",
            """
            # Default Stack
            - 默认：轻量 REST 服务
            """,
        )

        result = self.run_check()

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("开发类 Skill 缺少关键信息", result.stdout)
        self.assertIn("未验证项", result.stdout)
```

- [ ] **Step 2: Run tests to verify they fail**

Run:

```powershell
python -m unittest tests.test_check_skills -v
```

Expected: FAIL because `greenfield-bootstrap`, `android-app-scaffold`, and `backend-service-scaffold` are not yet recognized in `scripts/check_skills.py`.

- [ ] **Step 3: Update the development Skill registry**

In `scripts/check_skills.py`, extend `DEVELOPMENT_SKILLS` with the four new Skill names:

```python
DEVELOPMENT_SKILLS = {
    "android-development",
    "ios-development",
    "android-to-ios-bootstrap",
    "android-to-ios-porting",
    "api-design",
    "data-model-design",
    "technical-design",
    "test-case-generation",
    "build-ci-fix",
    "backend-development",
    "frontend-development",
    "greenfield-bootstrap",
    "android-app-scaffold",
    "ios-app-scaffold",
    "backend-service-scaffold",
}
```

- [ ] **Step 4: Run tests to verify they pass**

Run:

```powershell
python -m unittest tests.test_check_skills -v
```

Expected: PASS for all existing tests plus the new greenfield/scaffold test cases.

- [ ] **Step 5: Commit**

Run:

```powershell
git add scripts/check_skills.py tests/test_check_skills.py
git commit -m "补充 greenfield 与 scaffold skills 校验覆盖"
```

## Task 2: Add `greenfield-bootstrap`

**Files:**
- Create: `skills/greenfield-bootstrap/SKILL.md`
- Create: `skills/greenfield-bootstrap/bootstrap-checklist.md`

- [ ] **Step 1: Create the checklist file**

Create `skills/greenfield-bootstrap/bootstrap-checklist.md`:

```markdown
# Greenfield Bootstrap 检查清单

- [ ] 当前要启动的端有哪些：Android / iOS / Backend
- [ ] 是否需要多端并行推进
- [ ] 第一阶段是否必须依赖后端接口
- [ ] 是否已有原型、接口契约或数据结构约束
- [ ] 第一阶段是 demo 验证，还是可持续迭代的正式起盘
- [ ] 是否存在登录、支付、推送、上传、埋点、本地存储等基础能力要求
- [ ] 是否已有团队偏好的技术栈或目录规范
- [ ] 哪些信息仍然未知，必须写入未验证项
```

- [ ] **Step 2: Create the Skill file**

Create `skills/greenfield-bootstrap/SKILL.md`:

```markdown
---
name: greenfield-bootstrap
description: 用于在项目尚未创建时，判断 Android、iOS、Backend 的启动顺序、边界和后续 scaffold 路由。
---

# Greenfield Bootstrap Skill

## 适用场景

- 项目还没有创建，需要从 0 起盘
- 需要判断是单端启动还是多端联动启动
- 需要判断 Backend、Android、iOS 的推荐启动顺序
- 需要明确第一阶段边界、共享命名规则和后续 Skill 路由

## 输入

- 已确认的产品目标和第一阶段里程碑
- 项目入口文件和 `skills/common/`
- 已确认的需求分析或约束
- 是否包含 Android、iOS、Backend
- 是否存在原型、接口契约或数据结构约束
- `bootstrap-checklist.md`

## 工作流程

1. 阅读项目入口文件和 `skills/common/`。
2. 阅读第一阶段目标，确认这是单端启动还是多端联动启动。
3. 阅读 `bootstrap-checklist.md`，逐项判断端到端依赖。
4. 判断是否应默认以后端骨架优先，还是允许客户端先起 demo 壳子。
5. 输出第一阶段各端职责边界、共享命名规则、接口边界和禁止提前展开的范围。
6. 给出明确下一步 Skill 路由，例如 `technical-design`、`api-design`、`backend-service-scaffold`、`android-app-scaffold`、`ios-app-scaffold`。
7. 输出验证方式、未验证项和风险点。

## 输出格式

```text
【当前启动判断】
【推荐启动顺序】
【多端职责边界】
【共享命名与接口约束】
【推荐默认方案】
【备选方案与取舍】
【本阶段不应提前做的事】
【下一步建议 Skill】
【验证方式】
【未验证项】
【风险点】
```

## 约束

- 不直接承担 Android、iOS、Backend 的完整脚手架生成。
- 不跳过多端依赖判断就直接给出启动顺序。
- 不把缺少证据的产品假设写成确定结论。
- `bootstrap-checklist.md` 必须作为判断依据使用。
- 未确认的信息必须进入未验证项。

## 不适用场景

- 项目已经存在且只是继续开发
- Android 已有实现、当前只是补 iOS 的场景
- 已经进入某一端的具体编码阶段
```

- [ ] **Step 3: Run repo-level skill validation**

Run:

```powershell
python scripts\check_skills.py
```

Expected: `[OK] greenfield-bootstrap`

- [ ] **Step 4: Commit**

Run:

```powershell
git add skills/greenfield-bootstrap/SKILL.md skills/greenfield-bootstrap/bootstrap-checklist.md
git commit -m "新增 greenfield bootstrap skill"
```

## Task 3: Add `android-app-scaffold`

**Files:**
- Create: `skills/android-app-scaffold/SKILL.md`
- Create: `skills/android-app-scaffold/scaffold-checklist.md`
- Create: `skills/android-app-scaffold/default-stack.md`

- [ ] **Step 1: Create the support files**

Create `skills/android-app-scaffold/scaffold-checklist.md`:

```markdown
# Android App Scaffold 检查清单

- [ ] 当前是否真的需要多模块，而不是先单模块起步
- [ ] 第一阶段是否只需要最小可运行壳子
- [ ] 是否需要网络层、登录态、本地存储、埋点占位
- [ ] 是否已有团队偏好的包结构、命名规则和状态管理方式
- [ ] 是否需要兼容后续与 Backend、iOS 的数据结构对齐
- [ ] 哪些约束还不明确，必须写入未验证项
```

Create `skills/android-app-scaffold/default-stack.md`:

```markdown
# Android App Scaffold 默认栈

## 推荐默认方案

- Kotlin
- Jetpack Compose
- 单 app module 起步，按功能包分目录
- 预留 network / data / ui 边界

## 备选方案

- 需要严格模块边界时，再升级为多模块
- 如果项目明确要求 XML View，可切换到 XML + ViewModel

## 选择原则

- 第一批优先保证最小可运行、可扩展、可验证
- 没有明确约束时，不提前引入复杂模块化
```

- [ ] **Step 2: Create the Skill file**

Create `skills/android-app-scaffold/SKILL.md`:

```markdown
---
name: android-app-scaffold
description: 用于从 0 创建 Android 新项目骨架，确定默认栈、目录结构、首批文件和最小可运行壳子。
---

# Android App Scaffold Skill

## 适用场景

- 需要从 0 创建 Android 项目
- 需要确定 Android 第一阶段工程骨架
- 需要输出最小可运行页面、目录结构和基础配置
- 需要为后续 `android-development` 建立落点

## 输入

- 已确认的产品目标和第一阶段范围
- 已确认的技术方案
- 项目入口文件和 `skills/common/`
- `scaffold-checklist.md`
- `default-stack.md`

## 工作流程

1. 阅读项目入口文件和 `skills/common/`。
2. 阅读 `scaffold-checklist.md`，确认是否真的需要多模块和复杂分层。
3. 阅读 `default-stack.md`，先给推荐默认方案，再判断是否需要切换到备选方案。
4. 输出最小 Android 工程结构、首批目录、首批文件和基础配置。
5. 明确网络层、数据层、UI 层、路由层的最小边界。
6. 只生成最小可运行壳子，不提前展开完整业务代码。
7. 指向后续 `android-development` 的承接方式。
8. 输出验证方式、未验证项和风险点。

## 输出格式

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

## 约束

- `scaffold-checklist.md` 和 `default-stack.md` 必须一起使用。
- 不在第一阶段默认引入复杂多模块结构。
- 不把业务代码一次性铺满。
- 不能声称“已可运行”而没有给出验证方式。
- 缺少确认的信息必须进入未验证项。

## 不适用场景

- 已有稳定 Android 项目继续开发
- 只是现有 Android 功能的小改动
- 需求和技术方案仍未确认
```

- [ ] **Step 3: Run repo-level skill validation**

Run:

```powershell
python scripts\check_skills.py
```

Expected: `[OK] android-app-scaffold`

- [ ] **Step 4: Commit**

Run:

```powershell
git add skills/android-app-scaffold/SKILL.md skills/android-app-scaffold/scaffold-checklist.md skills/android-app-scaffold/default-stack.md
git commit -m "新增 android app scaffold skill"
```

## Task 4: Add `ios-app-scaffold`

**Files:**
- Create: `skills/ios-app-scaffold/SKILL.md`
- Create: `skills/ios-app-scaffold/scaffold-checklist.md`
- Create: `skills/ios-app-scaffold/default-stack.md`

- [ ] **Step 1: Create the support files**

Create `skills/ios-app-scaffold/scaffold-checklist.md`:

```markdown
# iOS App Scaffold 检查清单

- [ ] 当前是否只需要单工程起步，而不是复杂 workspace / 多 target
- [ ] 第一阶段是否只需要最小可运行壳子
- [ ] 是否需要网络层、登录态、本地持久化、埋点占位
- [ ] 是否存在未来与 Android 对齐的数据结构和交互约束
- [ ] 是否已有团队偏好的工程组织方式
- [ ] 哪些信息仍不明确，必须写入未验证项
```

Create `skills/ios-app-scaffold/default-stack.md`:

```markdown
# iOS App Scaffold 默认栈

## 推荐默认方案

- Swift
- SwiftUI
- 单工程起步
- 预留 view / state / service 边界

## 备选方案

- 如果项目明确要求 UIKit，可切换到 UIKit + ViewModel 风格
- 如果确实需要更强模块边界，再评估拆分 package 或 target

## 选择原则

- 第一批优先保证最小可运行、可扩展、可验证
- 没有明确约束时，不提前引入复杂工程组织
```

- [ ] **Step 2: Create the Skill file**

Create `skills/ios-app-scaffold/SKILL.md`:

```markdown
---
name: ios-app-scaffold
description: 用于从 0 创建 iOS 新项目骨架，确定默认栈、工程结构、首批文件和最小可运行壳子。
---

# iOS App Scaffold Skill

## 适用场景

- 需要从 0 创建 iOS 项目
- 需要确定 iOS 第一阶段工程骨架
- 需要输出最小可运行页面、目录结构和基础配置
- 需要为后续 `ios-development` 建立落点

## 输入

- 已确认的产品目标和第一阶段范围
- 已确认的技术方案
- 项目入口文件和 `skills/common/`
- `scaffold-checklist.md`
- `default-stack.md`

## 工作流程

1. 阅读项目入口文件和 `skills/common/`。
2. 阅读 `scaffold-checklist.md`，确认是否真的需要复杂 workspace、多 target 或额外模块化。
3. 阅读 `default-stack.md`，先给推荐默认方案，再判断是否需要切换到备选方案。
4. 输出最小 iOS 工程结构、首批目录、首批文件和基础配置。
5. 明确 view、state、service、navigation 的最小边界。
6. 只生成最小可运行壳子，不提前展开完整业务代码。
7. 指向后续 `ios-development` 的承接方式。
8. 输出验证方式、未验证项和风险点。

## 输出格式

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

## 约束

- `scaffold-checklist.md` 和 `default-stack.md` 必须一起使用。
- 不在第一阶段默认引入复杂 target 或 package 结构。
- 不把业务代码一次性铺满。
- 不能声称“已可运行”而没有给出验证方式。
- 缺少确认的信息必须进入未验证项。

## 不适用场景

- 已有稳定 iOS 项目继续开发
- Android 已有实现、当前只是补 iOS 的复刻场景
- 需求和技术方案仍未确认
```

- [ ] **Step 3: Run repo-level skill validation**

Run:

```powershell
python scripts\check_skills.py
```

Expected: `[OK] ios-app-scaffold`

- [ ] **Step 4: Commit**

Run:

```powershell
git add skills/ios-app-scaffold/SKILL.md skills/ios-app-scaffold/scaffold-checklist.md skills/ios-app-scaffold/default-stack.md
git commit -m "新增 ios app scaffold skill"
```

## Task 5: Add `backend-service-scaffold`

**Files:**
- Create: `skills/backend-service-scaffold/SKILL.md`
- Create: `skills/backend-service-scaffold/scaffold-checklist.md`
- Create: `skills/backend-service-scaffold/default-stack.md`

- [ ] **Step 1: Create the support files**

Create `skills/backend-service-scaffold/scaffold-checklist.md`:

```markdown
# Backend Service Scaffold 检查清单

- [ ] 第一阶段是否只需要单服务骨架
- [ ] 是否需要数据库、缓存、消息队列或外部依赖占位
- [ ] 是否需要鉴权、健康检查、统一错误处理、日志基线
- [ ] 是否已有接口契约或错误码约定
- [ ] 是否存在客户端依赖的返回结构和环境配置约束
- [ ] 哪些信息仍不明确，必须写入未验证项
```

Create `skills/backend-service-scaffold/default-stack.md`:

```markdown
# Backend Service Scaffold 默认栈

## 推荐默认方案

- 单服务起步
- 轻量 REST API
- 预留 config / route / service / test 边界
- 默认包含健康检查、统一错误处理和日志基线

## 备选方案

- 如果项目明确要求更强分层，可增加 handler / repository 等边界
- 如果第一阶段只是 mock 服务，可临时弱化持久化层

## 选择原则

- 第一批优先保证最小可运行、可扩展、可验证
- 没有明确约束时，不提前做微服务拆分
```

- [ ] **Step 2: Create the Skill file**

Create `skills/backend-service-scaffold/SKILL.md`:

```markdown
---
name: backend-service-scaffold
description: 用于从 0 创建服务端新项目骨架，确定默认栈、目录结构、首批文件和最小可运行 API 壳子。
---

# Backend Service Scaffold Skill

## 适用场景

- 需要从 0 创建服务端项目
- 需要确定服务端第一阶段工程骨架
- 需要输出健康检查、基础路由、配置和测试边界
- 需要为后续 `backend-development` 建立落点

## 输入

- 已确认的产品目标和第一阶段范围
- 已确认的技术方案和接口契约
- 项目入口文件和 `skills/common/`
- `scaffold-checklist.md`
- `default-stack.md`

## 工作流程

1. 阅读项目入口文件和 `skills/common/`。
2. 阅读 `scaffold-checklist.md`，确认第一阶段是否只需要单服务骨架。
3. 阅读 `default-stack.md`，先给推荐默认方案，再判断是否需要切换到备选方案。
4. 输出最小服务结构、首批目录、首批文件和基础配置。
5. 明确配置加载、健康检查、路由、错误处理、日志和首批测试边界。
6. 只生成最小可运行壳子，不提前展开完整业务逻辑。
7. 指向后续 `backend-development` 的承接方式。
8. 输出验证方式、未验证项和风险点。

## 输出格式

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

## 约束

- `scaffold-checklist.md` 和 `default-stack.md` 必须一起使用。
- 不在第一阶段默认展开微服务拆分。
- 不把业务逻辑一次性铺满。
- 不能声称“已可运行”而没有给出验证方式。
- 缺少确认的信息必须进入未验证项。

## 不适用场景

- 已有稳定服务继续开发
- 只是现有服务的小改动
- 需求、方案或接口契约仍未确认
```

- [ ] **Step 3: Run repo-level skill validation**

Run:

```powershell
python scripts\check_skills.py
```

Expected: `[OK] backend-service-scaffold`

- [ ] **Step 4: Commit**

Run:

```powershell
git add skills/backend-service-scaffold/SKILL.md skills/backend-service-scaffold/scaffold-checklist.md skills/backend-service-scaffold/default-stack.md
git commit -m "新增 backend service scaffold skill"
```

## Task 6: Route the New Workflow Through Docs and Adapters

**Files:**
- Modify: `README.md`
- Modify: `docs/getting-started.md`
- Modify: `docs/roadmap.md`
- Modify: `adapters/claude/CLAUDE.md.template`
- Modify: `adapters/codex/AGENTS.md.template`
- Modify: `adapters/cursor/cursor-rules.template.md`
- Modify: `adapters/generic/AI_AGENT.md.template`

- [ ] **Step 1: Update repository structure and routing docs**

In `README.md`, add the new directories near the startup/development Skills:

```text
│   ├── greenfield-bootstrap/               # 新项目起盘分流与多端启动判断
│   ├── android-app-scaffold/               # Android 新项目骨架
│   ├── ios-app-scaffold/                   # iOS 新项目骨架
│   ├── backend-service-scaffold/           # 服务端新项目骨架
```

Add a route near the usage guidance:

```text
如果项目还没有创建，建议先走：
context-bootstrap
→ greenfield-bootstrap
→ technical-design
→ api-design（如涉及服务端接口）
→ backend-service-scaffold
→ android-app-scaffold / ios-app-scaffold
→ backend-development / android-development / ios-development
```

Add platform entry examples:

```text
Android 新项目：android-app-scaffold
iOS 新项目：ios-app-scaffold
服务端新项目：backend-service-scaffold
多端从 0 起盘：greenfield-bootstrap
```

- [ ] **Step 2: Update the adapter templates**

In both `adapters/claude/CLAUDE.md.template` and `adapters/codex/AGENTS.md.template`, insert routing rows:

```markdown
| 新项目起盘 / 多端启动判断 | `.ai/ai-engineering-skills/skills/greenfield-bootstrap/SKILL.md` |
| Android 新项目骨架 | `.ai/ai-engineering-skills/skills/android-app-scaffold/SKILL.md` |
| iOS 新项目骨架 | `.ai/ai-engineering-skills/skills/ios-app-scaffold/SKILL.md` |
| 服务端新项目骨架 | `.ai/ai-engineering-skills/skills/backend-service-scaffold/SKILL.md` |
```

Add a default workflow note:

```text
如果任务是“从 0 创建 Android / iOS / Backend 项目”，默认先走：
greenfield-bootstrap
→ technical-design
→ api-design（如涉及服务端接口）
→ scaffold skill
→ development skill
```

In `adapters/cursor/cursor-rules.template.md`, add:

```markdown
如果是“从 0 创建 Android / iOS / Backend 项目”，优先读取 `greenfield-bootstrap`，再决定进入对应的 scaffold skill。
```

In `adapters/generic/AI_AGENT.md.template`, add:

```markdown
如果是“从 0 创建新项目”，优先读取 `greenfield-bootstrap`。
```

- [ ] **Step 3: Update getting-started and roadmap docs**

In `docs/getting-started.md`, add a new startup route:

```text
如果项目还没有创建，建议使用：
greenfield-bootstrap
→ technical-design
→ api-design（如涉及服务端接口）
→ backend-service-scaffold
→ android-app-scaffold / ios-app-scaffold
```

In `docs/roadmap.md`, add a stage item:

```text
- greenfield-bootstrap / android-app-scaffold / ios-app-scaffold / backend-service-scaffold 起盘链路
```

- [ ] **Step 4: Run full validation**

Run:

```powershell
python scripts\check_skills.py
python -m unittest tests.test_check_skills -v
rg -n "greenfield-bootstrap|android-app-scaffold|ios-app-scaffold|backend-service-scaffold" README.md docs adapters skills scripts tests
```

Expected:

```text
[OK] greenfield-bootstrap
[OK] android-app-scaffold
[OK] ios-app-scaffold
[OK] backend-service-scaffold
OK
```

- [ ] **Step 5: Commit**

Run:

```powershell
git add README.md docs/getting-started.md docs/roadmap.md adapters/claude/CLAUDE.md.template adapters/codex/AGENTS.md.template adapters/cursor/cursor-rules.template.md adapters/generic/AI_AGENT.md.template skills scripts tests
git commit -m "接入 greenfield 与 scaffold skills 路由"
```

## Task 7: Final Verification and Repository Summary

**Files:**
- Modify: none

- [ ] **Step 1: Verify working tree and latest commits**

Run:

```powershell
git status -sb
git log --oneline --decorate -5
```

Expected:

```text
## main
<recent commits for checker, four Skills, and routing docs>
```

- [ ] **Step 2: Run final repository checks**

Run:

```powershell
python scripts\check_skills.py
python -m unittest tests.test_check_skills -v
```

Expected:

```text
[OK] greenfield-bootstrap
[OK] android-app-scaffold
[OK] ios-app-scaffold
[OK] backend-service-scaffold
OK
```

- [ ] **Step 3: Prepare closeout notes**

Use this structure for the final implementation summary:

```text
【新增 Skills】
- greenfield-bootstrap
- android-app-scaffold
- ios-app-scaffold
- backend-service-scaffold

【文档与路由更新】
- README
- getting-started
- adapters

【验证结果】
- python scripts\check_skills.py
- python -m unittest tests.test_check_skills -v

【未验证项】
- 如果具体平台默认栈仍有待进一步业务验证，明确列出
```
