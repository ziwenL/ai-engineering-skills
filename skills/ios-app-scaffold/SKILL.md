---
name: ios-app-scaffold
description: 用于从 0 创建 iOS 新项目骨架，确定默认技术栈、工程结构、首批文件和最小可运行壳子，并衔接后续 ios-development。
---

# iOS App Scaffold Skill

## 适用场景

- 需要从 0 创建 iOS 新项目
- 需要为第一阶段里程碑搭建 iOS 工程骨架
- 需要明确默认技术栈、备选方案和切换条件
- 需要输出最小工程结构、首批目录与文件、最小可运行壳子和验证方式
- 需要为后续 `ios-development` 建立稳定落点

## 输入

- 已确认的产品目标、第一阶段范围和交付里程碑
- 已确认的技术方案、跨端约束和接口边界
- 项目入口文档和 `skills/common/`
- iOS 相关的团队规范、命名规则、依赖管理方式和相似实现
- 是否需要与 Android 保持行为、数据结构或错误处理对齐
- `scaffold-checklist.md`
- `default-stack.md`
- `usage-examples.md`

## 工作流程

1. 阅读项目入口文档和 `skills/common/`，确认当前任务是创建 iOS 新项目骨架，而不是继续修改已有 iOS 工程。
2. 阅读 `scaffold-checklist.md`，逐项判断第一阶段是否真的需要 `workspace`、多 `target`、本地 `Swift Package` 或额外模块化。
3. 阅读 `default-stack.md`，先给出推荐默认方案，再判断是否存在必须切换到备选方案的约束。
4. 明确第一阶段的目标是最小可运行壳子，而不是一次性铺开完整业务实现。
5. 输出推荐默认方案、备选方案与切换条件，并说明为什么默认采用单工程 + SwiftUI + 最小职责分层。
6. 定义最小工程结构，包括应用入口、主题或样式入口、首页壳、状态边界、服务边界、导航占位和资源目录。
7. 输出首批应创建的目录、文件和初始化步骤，并说明每一项存在的原因。
8. 明确 view、state、service、navigation 的最小边界，避免在 scaffold 阶段把业务细节提前固化。
9. 说明与 `ios-development` 的衔接方式。
10. 输出验证方式、未验证项和风险点。

## 输出格式

```text
【当前启动判断】
【推荐默认方案】
【备选方案与取舍】
【首批应创建的目录 / 文件】
【初始化步骤】
【最小边界说明】
【与 ios-development 的衔接方式】
【本阶段不应提前做的事】
【下一步建议 Skill】
【验证方式】
【未验证项】
【风险点】
```

## 约束

- 这是 iOS 新项目骨架层，不替代 `ios-development`，也不替代 `android-to-ios-bootstrap`。
- `scaffold-checklist.md` 和 `default-stack.md` 必须显式读取并作为判断依据使用。
- 第一阶段只创建最小可运行壳子，不默认引入复杂 `target`、`workspace`、本地 `Swift Package` 或额外依赖拆分。
- 不把业务代码一次性铺满；先收敛到工程入口、首批目录、最小页面壳和必要占位层。
- 没有明确证据时，不把未来跨端对齐要求、模块边界或依赖管理偏好写成既定事实。
- 不能声称“已验证”而没有给出验证方式；无法验证的部分必须进入未验证项。

## 不适用场景

- 已有稳定 iOS 项目，当前只是继续开发或局部改动。
- Android 已有实现，当前任务是判断是否应先创建或补齐 iOS 工程，此时应优先使用 `android-to-ios-bootstrap`。
- 当前更需要先做 `technical-design`、接口设计或 greenfield 启动分流，而不是直接起 iOS 骨架。
- 需求、范围或技术方向仍未确认，无法判断最小工程边界。

## 使用示例

最小调用示例：

```text
请使用 ios-app-scaffold skill，为当前需求创建 iOS 新项目骨架。

请先阅读：
1. 项目入口文档
2. skills/common/
3. 第一阶段目标
4. skills/ios-app-scaffold/scaffold-checklist.md
5. skills/ios-app-scaffold/default-stack.md

请输出：
1. 推荐默认方案
2. 首批应创建的目录 / 文件
3. 初始化步骤
4. 下一步建议 Skill
5. 验证方式
6. 未验证项

要求：
- 只创建最小可运行壳子。
- 不要提前展开完整业务逻辑。
```

更多示例见 `usage-examples.md`。
