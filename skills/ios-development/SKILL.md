---
name: ios-development
description: 用于 iOS 功能开发、Bug 修复、多端一致性实现和测试验证。
---

# iOS 开发 Skill

## 适用场景

- iOS 新功能开发
- iOS Bug 修复
- 多端一致性需求实现

## 输入

- 已确认的需求分析
- 已确认的技术方案
- iOS 相似实现
- `architecture.md`
- `checklist.md`
- `usage-examples.md`

## 工作流程

1. 阅读需求分析和技术方案。
2. 阅读 `architecture.md`，确认不绕过当前 iOS 架构。
3. 阅读 `checklist.md`，把它作为自检清单。
4. 查找 iOS 项目中的相似实现。
5. 如果是多端需求，提取平台无关行为。
6. 按 iOS 项目现有架构实现。
7. 明确状态处理、错误处理和空状态。
8. 输出验证方式、验证结果、未验证项和风险点。

## 输出格式

```text
【修改文件列表】
【每个文件的修改原因】
【核心实现逻辑】
【多端一致性要求】
【状态与异常处理】
【验证方式】
【未验证项】
【风险点】
```

## 约束

- 不机械翻译 Android 代码。
- 行为一致优先于结构一致。
- 不做无关重构。
- 必须使用 `architecture.md` 和 `checklist.md` 做自检。
- 没有验证证据时，要明确标记为“未验证项”。

## 不适用场景

- 纯 Android、服务端或前端任务。
- 尚未确认需求或方案的任务。

## 使用示例

最小调用示例：

```text
请使用 ios-development skill 实现该需求。

请先阅读：
1. 已确认的需求分析
2. 已确认的技术方案
3. skills/ios-development/architecture.md
4. skills/ios-development/checklist.md
5. iOS 项目中的相似实现

要求：
- 先查找相似实现。
- 遵守当前 iOS 架构。
- 如果涉及多端一致性，优先保证行为一致。
- 完成后给出验证方式、未验证项和风险点。
```

更多示例见 `usage-examples.md`。
