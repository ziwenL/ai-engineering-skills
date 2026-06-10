---
name: skill-authoring
description: 用于根据成功会话、踩坑经验和复盘结果生成或改进 Skill。
---

# Skill 生成与迭代 Skill

## 适用场景

- 需要新增 Skill
- 需要优化已有 Skill
- 需要把高频经验沉淀为流程
- 需要把旧 Prompt 改造成标准 Skill

## 输入

- session-retrospective 输出
- 已验证的会话经验
- 目标 Skill 或待新增 Skill 的定位
- 如有辅助文件，也要同时规划它们与主 `SKILL.md` 的关系

## 工作流程

1. 阅读 session-retrospective 输出。
2. 判断是更新 common、更新已有 Skill，还是新增 Skill。
3. 只沉淀已验证、可复用、长期有效内容。
4. 如需 `checklist.md`、`architecture.md`、`log-analysis.md` 等辅助文件，明确它们的职责。
5. 生成标准 `SKILL.md`，并确保主文件显式引用这些辅助文件。
6. 输出变更理由、风险和需要同步修改的文件。
7. 建议由 code-review skill 审查 Skill 本身。

## 输出格式

```text
【建议修改位置】
【修改原因】
【主文件 patch】
【辅助文件 patch】
【风险】
【是否需要同步修改 common 或入口文件】
```

## 约束

- 只沉淀已验证、可复用、长期有效内容。
- 不写入密钥、Token、隐私、临时日志、未验证猜测。
- 主 `SKILL.md` 不能与辅助文件失联。

## 不适用场景

- 只是一次性经验、还未验证是否可复用
- 纯项目特有规则且不适合进入公共 Skill

## 标准 Skill 结构

```text
frontmatter:
  name
  description

正文：
  适用场景
  输入
  工作流程
  输出格式
  约束
  不适用场景
```
