---
name: android-app-scaffold
description: 用于从 0 创建 Android 新项目骨架，确定默认技术栈、最小工程结构、首批文件和最小可运行壳子，并衔接后续 android-development。
---

# Android App Scaffold Skill

## 适用场景

- 需要从 0 创建 Android 新项目
- 需要为第一阶段里程碑搭建 Android 工程骨架
- 需要明确默认技术栈、备选方案和切换条件
- 需要输出最小工程结构、首批目录与文件、最小可运行壳子和验证方式
- 需要为后续 `android-development` 建立稳定落点

## 输入

- 已确认的产品目标、第一阶段范围和交付里程碑
- 已确认的技术方案、跨端约束和接口边界
- 项目入口文档和 `skills/common/`
- Android 相关的团队规范、包结构偏好、构建约束和相似实现
- `scaffold-checklist.md`
- `default-stack.md`
- `usage-examples.md`

## 工作流程

1. 阅读项目入口文档和 `skills/common/`，确认当前任务是创建 Android 新项目骨架，而不是继续修改已有 Android 工程。
2. 阅读 `scaffold-checklist.md`，逐项确认第一阶段是否真的需要多模块、复杂分层或完整业务页面。
3. 阅读 `default-stack.md`，先给出推荐默认方案，再判断是否存在必须切换到备选方案的约束。
4. 明确第一阶段的目标是最小可运行壳子，而不是一次性铺开完整业务实现。
5. 输出推荐默认方案、备选方案与切换条件，并说明为什么默认采用单 `app` 模块加按功能包组织的目录策略。
6. 定义最小工程结构，包括应用入口、主题、基础页面壳、网络占位、数据边界和路由占位。
7. 输出首批应创建的目录、模块、文件和初始化步骤，并说明每一项存在的原因。
8. 明确本阶段不应提前做的事，例如过早拆分模块、补齐完整业务流、引入复杂发布或 CI 配置。
9. 说明与 `android-development` 的衔接方式。
10. 输出验证方式、未验证项和风险点。

## 输出格式

```text
【当前启动判断】
【推荐默认方案】
【备选方案与取舍】
【首批应创建的目录 / 模块 / 文件】
【初始化步骤】
【最小边界说明】
【与 android-development 的衔接方式】
【本阶段不应提前做的事】
【下一步建议 Skill】
【验证方式】
【未验证项】
【风险点】
```

## 约束

- 这是 Android 新项目骨架层，不替代 `technical-design`，也不替代 `android-development`。
- `scaffold-checklist.md` 和 `default-stack.md` 必须显式读取并作为判断依据使用。
- 第一阶段只创建最小可运行壳子，不默认引入复杂多模块、组件化或发布流水线。
- 不能一次性铺开完整业务代码，必须先收敛到最小工程结构和首批文件。
- 没有明确证据时，不把技术偏好、模块边界或未来扩展路径写成既定事实。
- 不能声称“已验证”而没有给出验证方式；无法验证的部分必须进入未验证项。

## 不适用场景

- 已有稳定 Android 项目，当前只是继续开发或局部改动。
- 当前更需要先做 `technical-design`、接口设计或跨端启动分流，而不是直接起 Android 骨架。
- Android 只是已有实现中的小改动，不需要新建工程。
- 需求、范围或技术方向仍未确认，无法决定最小骨架边界。

## 使用示例

最小调用示例：

```text
请使用 android-app-scaffold skill，为当前需求创建 Android 新项目骨架。

请先阅读：
1. 项目入口文档
2. skills/common/
3. 第一阶段目标
4. skills/android-app-scaffold/scaffold-checklist.md
5. skills/android-app-scaffold/default-stack.md

请输出：
1. 推荐默认方案
2. 首批应创建的目录 / 模块 / 文件
3. 初始化步骤
4. 下一步建议 Skill
5. 验证方式
6. 未验证项

要求：
- 只创建最小可运行壳子。
- 不要提前展开完整业务逻辑。
```

更多示例见 `usage-examples.md`。
