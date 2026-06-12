# Skill Usage Examples First Batch Plan

> **For agentic workers:** Use `superpowers:writing-skills` while updating these Skills, and verify repository validation before claiming completion.

**Goal:** 为首批 5 个高频 Skill 增加统一的调用示例层，包括 `SKILL.md` 中的最小示例入口，以及 Skill 目录下的 `usage-examples.md`。

**Scope:** `context-bootstrap`、`technical-design`、`android-development`、`ios-development`、`backend-development`

---

## File Map

- Create: `docs/superpowers/specs/2026-06-12-skill-usage-examples-design.md`
- Create: `docs/superpowers/plans/2026-06-12-skill-usage-examples-first-batch-plan.md`
- Create: `skills/context-bootstrap/usage-examples.md`
- Create: `skills/technical-design/usage-examples.md`
- Create: `skills/android-development/usage-examples.md`
- Create: `skills/ios-development/usage-examples.md`
- Create: `skills/backend-development/usage-examples.md`
- Modify: `skills/context-bootstrap/SKILL.md`
- Modify: `skills/technical-design/SKILL.md`
- Modify: `skills/android-development/SKILL.md`
- Modify: `skills/ios-development/SKILL.md`
- Modify: `skills/backend-development/SKILL.md`
- Modify: `docs/skill-writing-guide.md`

## Task 1: 固化写法约定

- [ ] 在 `docs/skill-writing-guide.md` 中补充“调用示例层”约定
- [ ] 明确 `SKILL.md` 与 `usage-examples.md` 的分工
- [ ] 明确 `usage-examples.md` 的统一结构

## Task 2: 为 5 个 Skill 新增详细示例文件

- [ ] 创建 `skills/context-bootstrap/usage-examples.md`
- [ ] 创建 `skills/technical-design/usage-examples.md`
- [ ] 创建 `skills/android-development/usage-examples.md`
- [ ] 创建 `skills/ios-development/usage-examples.md`
- [ ] 创建 `skills/backend-development/usage-examples.md`

每个文件都应包含：

- `## 说明`
- `## 最小调用示例`
- `## 推荐调用示例`
- `## 高约束调用示例`
- `## 适用提醒`

## Task 3: 在 `SKILL.md` 中补最小入口

- [ ] 在 5 个 Skill 的 `SKILL.md` 中新增 `## 使用示例`
- [ ] 每个 Skill 至少补一个最小调用示例
- [ ] 显式引用 `usage-examples.md`

## Task 4: 验证

- [ ] 运行 `python scripts\check_skills.py`
- [ ] 检查 5 个 Skill 的 `SKILL.md` 中都已出现 `usage-examples.md`
- [ ] 检查新增文件都已落盘

## Closeout

最终说明应覆盖：

- 本轮新增了哪些 `usage-examples.md`
- 哪些 `SKILL.md` 已补最小调用示例
- 校验是否通过
- 尚未覆盖的 Skill 范围
