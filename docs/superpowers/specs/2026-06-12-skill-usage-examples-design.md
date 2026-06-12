# Skill Usage Examples Design

## Goal

为仓库中的 Skill 增加一层稳定、可复制的“调用示例”能力，降低用户在实际使用时自行组织提示词的成本。

第一批先覆盖 5 个高频 Skill：

- `context-bootstrap`
- `technical-design`
- `android-development`
- `ios-development`
- `backend-development`

## Problem

当前仓库中的 Skill 已经具备较明确的职责、输入和输出约束，但从真实使用体验看，用户仍然需要自己补齐一段“怎么调用这个 Skill”的提示词。

这会带来几个问题：

- 新用户知道“该用哪个 Skill”，但不知道“怎么发起一次高质量调用”。
- 老用户会重复手写相似指令，容易出现遗漏约束、输出结构不稳定、上下文输入不完整的问题。
- 同一个 Skill 在不同会话里的调用方式漂移较大，不利于沉淀为团队级的标准工作流。

因此，Skill 本体之外还需要一层更贴近实战的调用示例。

## Design Decision

采用双层结构：

1. 在 `SKILL.md` 中内置一个最小调用示例，保证用户打开 Skill 就能立刻复制使用。
2. 在 Skill 目录下新增 `usage-examples.md`，沉淀更完整的多场景示例。

结构如下：

```text
skills/<skill-name>/
├── SKILL.md
└── usage-examples.md
```

## Why Two Layers

只把示例写进 `SKILL.md` 会让主文档逐渐臃肿，影响快速扫描。

只单独放 `usage-examples.md` 又会让用户第一次打开 Skill 时缺少立即可用的入口。

双层结构兼顾：

- `SKILL.md` 负责“立刻可用”
- `usage-examples.md` 负责“覆盖更多场景”

## `SKILL.md` Convention

每个接入示例层的 Skill，需要在 `SKILL.md` 中新增一个简短的“使用示例”区块，包含：

- 一个最小调用示例
- 一句“更多示例见 `usage-examples.md`”

这样既能满足快速复制，也能满足仓库校验器对辅助文件引用的要求。

## `usage-examples.md` Convention

首批统一结构如下：

```text
# 使用示例
## 说明
## 最小调用示例
## 推荐调用示例
## 高约束调用示例
## 适用提醒
```

其中：

- `最小调用示例`：最短可用版本
- `推荐调用示例`：日常最值得复制的版本
- `高约束调用示例`：适合要求输出结构稳定、约束更严的版本
- `适用提醒`：说明这些示例分别适合什么场景

## Example Writing Rules

调用示例必须是“可直接复制的提示词”，而不是解释性文字。

每个示例尽量包含这几类元素：

- 明确指定 Skill 名称
- 指定先阅读哪些上下文
- 指定要输出什么结构
- 指定不能做什么或必须遵守什么约束

示例内容应尽量避免：

- 空泛指令
- 模糊输出要求
- 让模型自行猜测项目事实
- 与 Skill 职责不符的要求

## First-Batch Scope

这次只处理 5 个核心 Skill：

- `context-bootstrap`
- `technical-design`
- `android-development`
- `ios-development`
- `backend-development`

暂不批量覆盖所有 Skill，避免一次性扩散过大，先把模板、位置和写法稳定下来。

## Out of Scope

这次不做：

- 为所有 Skill 一次性补齐示例
- 在 README 中为每个 Skill 再复制一遍完整示例
- 改造校验器去强制要求所有 Skill 都必须有 `usage-examples.md`
- 系统性修复仓库中历史文档编码问题

## Success Criteria

本轮工作完成后，应满足：

1. 首批 5 个 Skill 都有 `usage-examples.md`
2. 对应 `SKILL.md` 都有最小调用示例和引用入口
3. `docs/skill-writing-guide.md` 明确记录这套约定
4. `python scripts/check_skills.py` 校验通过
