# 使用示例

## 说明

这个 Skill 适合在项目尚未创建时，先判断是单端还是多端起盘、谁先启动、每一端的边界是什么，以及后续应进入哪些 scaffold Skill。

## 最小调用示例

```text
请使用 greenfield-bootstrap skill，判断当前项目应如何从 0 起盘。

已知信息：
1. 产品目标
2. 第一阶段里程碑
3. 目标端范围：Android / iOS / Backend
4. 是否已有 API 契约或原型

请输出：
1. 当前启动判断
2. 推荐启动顺序
3. 多端职责边界
4. 下一步建议 Skill
5. 验证方式
6. 未验证项

要求：
- 不要直接展开完整实现。
- 缺信息时不要猜测，写进未验证项。
```

## 推荐调用示例

```text
请使用 greenfield-bootstrap skill，判断这个项目从 0 起盘时的合理启动方式。

请先阅读：
1. 项目入口文档
2. skills/common/
3. 第一阶段目标与里程碑
4. 目标端范围：Android / iOS / Backend
5. 已知产品能力需求，例如登录、支付、上传、推送、本地存储
6. 已知团队技术偏好和交付约束
7. skills/greenfield-bootstrap/bootstrap-checklist.md

请输出：
1. 当前启动判断
2. 推荐启动顺序
3. 多端职责边界
4. 共享命名与接口约束
5. 推荐默认方案
6. 备选方案与取舍
7. 本阶段不应提前做的事
8. 下一步建议 Skill
9. 验证方式
10. 未验证项
11. 风险点

要求：
- 这是 greenfield 分流，不是直接开始大规模 scaffold 或实现。
- 必须显式使用 bootstrap-checklist.md 做判断。
- 不要把产品或技术假设写成确定事实。
```

## 高约束调用示例

```text
请使用 greenfield-bootstrap skill，严格判断当前项目从 0 起盘的启动顺序和路由。

必须先阅读：
1. 项目入口文档
2. skills/common/
3. 第一阶段目标与里程碑
4. 目标端范围
5. 已知能力需求与交付约束
6. skills/greenfield-bootstrap/bootstrap-checklist.md

请严格按以下结构输出：
【当前启动判断】
【推荐启动顺序】
【多端职责边界】
【共享命名与接口约束】
【推荐默认方案】
【备选方案与取舍】
【本阶段不应提前做的事】
【下一步建议 Skill】
【验证方式】
【未验证项】
【风险点】

要求：
- 不要直接承担 Android / iOS / Backend 的完整 scaffold 或实现。
- 不要跳过跨端依赖判断。
- 所有未确认信息必须进入【未验证项】。
```

## 适用提醒

- 适合项目还没创建时的总分流判断。
- 如果已经明确要起某一端具体工程，下一步通常切到对应 scaffold Skill。
- 如果 Android 已经存在、只是补 iOS，不要用它，改用 `android-to-ios-bootstrap`。
