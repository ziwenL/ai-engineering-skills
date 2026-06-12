# 使用示例

## 说明

这个 Skill 适合从 0 起一个 iOS 新项目骨架，先确定默认技术栈、工程结构和最小可运行壳子，再衔接到后续 `ios-development`。

## 最小调用示例

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

## 推荐调用示例

```text
请使用 ios-app-scaffold skill，为当前项目从 0 起一个 iOS 工程骨架。

请先阅读：
1. 产品目标与第一阶段范围
2. 已确认的技术方案、跨端约束和接口边界
3. 项目入口文档和 skills/common/
4. 团队 iOS 规范、命名规则、依赖管理方式和相似实现
5. 是否需要与 Android 保持行为、数据结构或错误处理对齐
6. skills/ios-app-scaffold/scaffold-checklist.md
7. skills/ios-app-scaffold/default-stack.md

请输出：
1. 当前启动判断
2. 推荐默认方案
3. 备选方案与取舍
4. 首批应创建的目录 / 文件
5. 初始化步骤
6. 最小边界说明
7. 与 ios-development 的衔接方式
8. 本阶段不应提前做的事
9. 下一步建议 Skill
10. 验证方式
11. 未验证项
12. 风险点

要求：
- scaffold-checklist.md 和 default-stack.md 必须显式使用。
- 这是骨架层，不是完整业务实现层。
- 不要把未来跨端对齐要求直接写成已验证事实。
```

## 高约束调用示例

```text
请使用 ios-app-scaffold skill，严格为当前项目设计 iOS 新项目骨架。

必须先阅读：
1. 产品目标与第一阶段范围
2. 技术方案与跨端约束
3. 项目入口文档和 skills/common/
4. 团队 iOS 规范
5. skills/ios-app-scaffold/scaffold-checklist.md
6. skills/ios-app-scaffold/default-stack.md

请严格按以下结构输出：
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

要求：
- 只创建最小可运行壳子。
- 不要默认展开复杂 workspace / target / package 结构。
- 无法验证的信息必须进入【未验证项】。
```

## 适用提醒

- 适合 iOS 项目还不存在时使用。
- 如果只是继续开发已有 iOS 项目，应切到 `ios-development`。
- 如果当前任务是 Android 已有、iOS 需要补建复刻链路，应优先看 `android-to-ios-bootstrap`。
