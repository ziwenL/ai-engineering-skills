# Android-to-iOS Bootstrap Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a new `android-to-ios-bootstrap` Skill that routes users correctly when Android functionality exists but iOS project readiness is unknown, missing, or incomplete.

**Architecture:** The new Skill will sit in front of `android-to-ios-porting` and `ios-development`. It will classify iOS-side readiness into three scenarios, use a dedicated bootstrap checklist, and route users to the correct next Skill. Repository docs and adapter templates will be updated so this new entrypoint is discoverable and consistent.

**Tech Stack:** Markdown Skills, repository docs/templates, Python checker validation, unittest

---

### Task 1: Add Checker Coverage For The New Skill

**Files:**
- Modify: `tests/test_check_skills.py`
- Modify: `scripts/check_skills.py`

- [ ] **Step 1: Write the failing tests**

Add test cases covering:

- a valid `android-to-ios-bootstrap` Skill that references `bootstrap-checklist.md`
- a failing case where `bootstrap-checklist.md` exists but is not referenced
- a failing case where the Skill lacks verification / unverified-item language

Use this structure in `tests/test_check_skills.py`:

```python
    def test_passes_for_android_to_ios_bootstrap_with_referenced_checklist(self) -> None:
        write_text(
            self.temp_dir / "skills" / "android-to-ios-bootstrap" / "SKILL.md",
            """
            ---
            name: android-to-ios-bootstrap
            description: 示例
            ---

            # Android 到 iOS 启动 Skill

            ## 适用场景
            - Android 已有实现，iOS 状态不明确

            ## 输入
            - Android 代码
            - `bootstrap-checklist.md`

            ## 工作流程
            1. 读取 `bootstrap-checklist.md`
            2. 判断 iOS 状态

            ## 输出格式
            ```text
            【建议下一步 Skill】
            【验证方式】
            【未验证项】
            ```

            ## 约束
            - 不要直接进入完整实现

            ## 不适用场景
            - Android 尚未稳定
            """,
        )
        write_text(
            self.temp_dir / "skills" / "android-to-ios-bootstrap" / "bootstrap-checklist.md",
            """
            # Bootstrap Checklist
            - [ ] iOS 项目是否存在
            """,
        )

        result = self.run_check()

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
```

```python
    def test_fails_when_android_to_ios_bootstrap_checklist_is_not_referenced(self) -> None:
        ...
        self.assertIn("未引用的辅助文件", result.stdout)
        self.assertIn("bootstrap-checklist.md", result.stdout)
```

```python
    def test_fails_when_android_to_ios_bootstrap_lacks_unverified_item_language(self) -> None:
        ...
        self.assertIn("开发类 Skill 缺少关键信息", result.stdout)
        self.assertIn("未验证项", result.stdout)
```

- [ ] **Step 2: Run test to verify it fails**

Run:

```powershell
python -m unittest tests.test_check_skills -v
```

Expected:

```text
FAIL for one or more new android-to-ios-bootstrap cases
```

- [ ] **Step 3: Update checker support if needed**

If the checker needs explicit awareness of the new Skill category, update `scripts/check_skills.py` by including `android-to-ios-bootstrap` in the development-skill set:

```python
DEVELOPMENT_SKILLS = {
    "android-development",
    "ios-development",
    "android-to-ios-porting",
    "android-to-ios-bootstrap",
    "api-design",
    "data-model-design",
    "technical-design",
    "test-case-generation",
    "build-ci-fix",
    "backend-development",
    "frontend-development",
}
```

- [ ] **Step 4: Run test to verify it passes**

Run:

```powershell
python -m unittest tests.test_check_skills -v
```

Expected:

```text
All tests pass
```

- [ ] **Step 5: Commit**

```bash
git add tests/test_check_skills.py scripts/check_skills.py
git commit -m "add checker coverage for android-to-ios-bootstrap"
```

### Task 2: Create The New Skill And Bootstrap Checklist

**Files:**
- Create: `skills/android-to-ios-bootstrap/SKILL.md`
- Create: `skills/android-to-ios-bootstrap/bootstrap-checklist.md`

- [ ] **Step 1: Write the Skill file**

Create `skills/android-to-ios-bootstrap/SKILL.md` with this content:

```md
---
name: android-to-ios-bootstrap
description: 用于在 Android 已有实现的前提下，判断 iOS 端是否需要先创建工程、补齐结构，或直接进入复刻流程。
---

# Android 到 iOS 启动 Skill

## 适用场景

- Android 端已有稳定实现，但 iOS 项目还没创建
- iOS 项目已创建，但结构是否足以承接功能仍不明确
- 需要判断应该先建壳、先补架构，还是直接进入复刻

## 输入

- Android 已实现代码
- 已确认的产品需求和交互要求
- 已知平台差异和限制
- iOS 当前状态信息：
  - 尚未创建
  - 已创建但结构未稳定
  - 已创建且已有可复用结构
- 如果 iOS 项目已存在：
  - 目录结构
  - 当前架构模式
  - 相似模块
- `bootstrap-checklist.md`

## 工作流程

1. 阅读 Android 已实现代码，识别用户可感知行为。
2. 提取平台无关逻辑，包括流程、状态模型、接口交互、错误处理和埋点。
3. 阅读 `bootstrap-checklist.md`，检查 iOS 当前工程状态。
4. 将当前场景判断为以下三类之一：
   - iOS 项目未创建
   - iOS 项目已创建但结构未稳定
   - iOS 项目已创建且可直接复刻
5. 如果 iOS 项目未创建：
   - 输出建议的最小 iOS 工程结构
   - 输出首批应创建的目录、模块和文件
   - 建议下一步先补 iOS 工程骨架，再进入 `ios-development`
6. 如果 iOS 项目已创建但结构未稳定：
   - 输出最小结构补齐方案
   - 标记哪些能力必须先稳定
   - 建议下一步先补结构，再进入 `android-to-ios-porting`
7. 如果 iOS 项目已创建且可直接复刻：
   - 说明为什么可以直接复刻
   - 建议下一步进入 `android-to-ios-porting`，再进入 `ios-development`
8. 输出验证方式、未验证项和风险点。

## 输出格式

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

## 约束

- 不直接承担完整 iOS 功能实现。
- 不机械翻译 Android 代码。
- 行为一致优先于结构一致。
- 不要伪造 iOS 架构事实。
- 无法确认的工程状态必须写入“未验证项”。

## 不适用场景

- Android 端还没有稳定实现
- 需求本身尚未确认
- 已经进入 iOS 具体编码阶段且项目结构清晰
```

- [ ] **Step 2: Write the support checklist**

Create `skills/android-to-ios-bootstrap/bootstrap-checklist.md` with this content:

```md
# Android 到 iOS 启动检查清单

- [ ] Android 端功能是否已经稳定实现
- [ ] 是否已确认产品需求和交互要求
- [ ] iOS 项目是否已经创建
- [ ] 如果已创建，是否已有稳定目录结构
- [ ] 如果已创建，是否已有可复用的状态管理方式
- [ ] 如果已创建，是否已有网络层和错误处理约定
- [ ] 如果已创建，是否已有相似页面或模块
- [ ] 当前是否可以直接进入复刻，而不是先补工程骨架
```

- [ ] **Step 3: Run checker to verify the new files pass**

Run:

```powershell
python scripts/check_skills.py
```

Expected:

```text
[OK] android-to-ios-bootstrap
```

- [ ] **Step 4: Commit**

```bash
git add skills/android-to-ios-bootstrap/SKILL.md skills/android-to-ios-bootstrap/bootstrap-checklist.md
git commit -m "add android-to-ios-bootstrap skill"
```

### Task 3: Integrate The New Skill Into Adapter Routing

**Files:**
- Modify: `adapters/claude/CLAUDE.md.template`
- Modify: `adapters/codex/AGENTS.md.template`
- Modify: `adapters/cursor/cursor-rules.template.md`

- [ ] **Step 1: Add the new skill route to Claude/Codex templates**

In both adapter templates, add a route row near the iOS-related rows:

```md
| Android 已有实现但 iOS 状态未明 | `.ai/ai-engineering-skills/skills/android-to-ios-bootstrap/SKILL.md` |
```

- [ ] **Step 2: Add routing guidance to Cursor rules**

Update the Cursor rules so iOS bootstrap is explicitly discoverable:

```md
2. 根据任务读取对应 Skill；如果是 “Android 已有实现，但 iOS 项目未创建或结构不明确”，优先读取 `android-to-ios-bootstrap`。
```

- [ ] **Step 3: Run a quick content check**

Run:

```powershell
rg -n "android-to-ios-bootstrap" adapters
```

Expected:

```text
New skill appears in all adapter entry files
```

- [ ] **Step 4: Commit**

```bash
git add adapters/claude/CLAUDE.md.template adapters/codex/AGENTS.md.template adapters/cursor/cursor-rules.template.md
git commit -m "route adapters to android-to-ios-bootstrap"
```

### Task 4: Update Repository Docs And User Guidance

**Files:**
- Modify: `README.md`
- Modify: `docs/getting-started.md`
- Modify: `docs/roadmap.md`

- [ ] **Step 1: Update README skill descriptions and usage flow**

Add the new Skill to the repository structure section:

```text
│   ├── android-to-ios-bootstrap/            # Android 已有实现时的 iOS 启动与分流
│   ├── android-to-ios-porting/              # Android 到 iOS 复刻
```

Add usage guidance near the iOS / multi-end workflow:

```text
如果 Android 功能已经完成，但 iOS 端项目尚未创建或结构不清晰：
context-bootstrap
→ android-to-ios-bootstrap
→ android-to-ios-porting
→ ios-development
```

Add scenario notes:

```text
1. iOS 项目未创建：先用 android-to-ios-bootstrap 判断骨架与首批模块
2. iOS 项目已创建但不稳定：先用 android-to-ios-bootstrap 补结构
3. iOS 项目已创建且稳定：可直接由 android-to-ios-bootstrap 路由到 android-to-ios-porting
```

- [ ] **Step 2: Update getting-started guidance**

Add a short section explaining when this Skill is the right entrypoint:

```md
## Android 到 iOS 的补充入口

如果 Android 端功能已经存在，但 iOS 端项目还没创建，或者你不确定当前 iOS 工程是否足以承接功能，先使用：

```text
android-to-ios-bootstrap
```

再根据输出进入：

- `android-to-ios-porting`
- `ios-development`
```

- [ ] **Step 3: Update roadmap**

Add the new Skill into the roadmap where cross-platform replication becomes more systematic:

```md
- android-to-ios-bootstrap
```

- [ ] **Step 4: Run a content check**

Run:

```powershell
rg -n "android-to-ios-bootstrap" README.md docs adapters
```

Expected:

```text
The new skill is documented in README, docs, and adapter templates
```

- [ ] **Step 5: Commit**

```bash
git add README.md docs/getting-started.md docs/roadmap.md
git commit -m "document android-to-ios-bootstrap workflow"
```

### Task 5: Final Verification

**Files:**
- Verify only

- [ ] **Step 1: Run unit tests**

Run:

```powershell
python -m unittest tests.test_check_skills -v
```

Expected:

```text
All tests pass
```

- [ ] **Step 2: Run repository checker**

Run:

```powershell
python scripts/check_skills.py
```

Expected:

```text
All skills report [OK], including android-to-ios-bootstrap
```

- [ ] **Step 3: Inspect git status**

Run:

```powershell
git status --short
```

Expected:

```text
Only the intended new-skill and documentation changes are present
```

- [ ] **Step 4: Commit**

```bash
git add skills/android-to-ios-bootstrap adapters README.md docs tests scripts
git commit -m "add android-to-ios bootstrap workflow"
```
