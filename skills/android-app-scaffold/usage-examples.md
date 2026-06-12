# 使用示例

## 说明

这个 Skill 适合从 0 起一个 Android 新项目骨架，先明确默认技术栈、首批目录和最小可运行壳子，而不是直接铺开完整业务实现。

## 最小调用示例

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

## 推荐调用示例

```text
请使用 android-app-scaffold skill，为当前项目从 0 起一个 Android 工程骨架。

请先阅读：
1. 产品目标与第一阶段范围
2. 已确认的技术方案、跨端约束和接口边界
3. 项目入口文档和 skills/common/
4. 团队 Android 规范、包结构偏好、构建约束和相似实现
5. skills/android-app-scaffold/scaffold-checklist.md
6. skills/android-app-scaffold/default-stack.md

请输出：
1. 当前启动判断
2. 推荐默认方案
3. 备选方案与取舍
4. 首批应创建的目录 / 模块 / 文件
5. 初始化步骤
6. 最小边界说明
7. 与 android-development 的衔接方式
8. 本阶段不应提前做的事
9. 下一步建议 Skill
10. 验证方式
11. 未验证项
12. 风险点

要求：
- scaffold-checklist.md 和 default-stack.md 必须显式使用。
- 这是骨架层，不是完整业务实现层。
- 没有证据时，不要把模块边界或技术偏好写成既定事实。
```

## 高约束调用示例

```text
请使用 android-app-scaffold skill，严格为当前项目设计 Android 新项目骨架。

必须先阅读：
1. 产品目标与第一阶段范围
2. 技术方案与跨端约束
3. 项目入口文档和 skills/common/
4. 团队 Android 规范
5. skills/android-app-scaffold/scaffold-checklist.md
6. skills/android-app-scaffold/default-stack.md

请严格按以下结构输出：
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

要求：
- 只创建最小可运行壳子。
- 不要默认展开复杂多模块结构。
- 无法验证的信息必须进入【未验证项】。
```

## 适用提醒

- 适合 Android 项目还不存在时使用。
- 如果只是继续开发已有 Android 项目，应切到 `android-development`。
- 如果项目还没完成总分流判断，应先用 `greenfield-bootstrap`。
