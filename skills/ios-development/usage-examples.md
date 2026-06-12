# 使用示例

## 说明

这个 Skill 适合在已有 iOS 项目中做功能开发、Bug 修复或与 Android 行为对齐。示例强调遵守当前 iOS 架构，并优先保证行为一致而不是机械翻译实现。

## 最小调用示例

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

## 推荐调用示例

```text
请使用 ios-development skill 在当前 iOS 项目中实现这个需求。

请按以下顺序进行：
1. 阅读需求分析和技术方案
2. 阅读 skills/ios-development/architecture.md
3. 阅读 skills/ios-development/checklist.md
4. 查找 iOS 项目中的相似实现
5. 如果是多端需求，提取 Android 或产品定义中的平台无关行为

实现要求：
1. 先列出计划修改的文件和原因
2. 遵守当前 iOS 项目架构
3. 不要机械翻译 Android 代码
4. 明确状态处理、错误处理和空状态
5. 不做与当前需求无关的重构

完成后请输出：
1. 修改文件列表
2. 核心实现逻辑
3. 多端一致性要求
4. 状态与异常处理
5. 验证方式
6. 未验证项
7. 风险点
```

## 高约束调用示例

```text
请使用 ios-development skill 实现当前需求，并保持 iOS 原生架构与多端行为一致性。

必须先阅读：
1. 已确认的需求分析
2. 已确认的技术方案
3. skills/ios-development/architecture.md
4. skills/ios-development/checklist.md
5. iOS 项目中的相似实现
6. 如果涉及多端，补充阅读 Android 或接口侧的行为定义

执行要求：
- 先输出计划修改文件清单，不要直接开改。
- 行为一致优先于代码结构一致。
- 不要为了“和 Android 一样”而破坏 iOS 项目现有组织方式。

请严格按以下结构输出：
【修改文件列表】
【每个文件的修改原因】
【核心实现逻辑】
【多端一致性要求】
【状态与异常处理】
【验证方式】
【未验证项】
【风险点】
```

## 适用提醒

- 适合已有 iOS 项目中的开发与修复。
- 如果 iOS 项目尚未创建，应优先使用 `ios-app-scaffold`。
- 如果场景是“Android 已有实现，需要补建 iOS 路由与约束”，优先看 `android-to-ios-bootstrap`。
