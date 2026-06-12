# 使用示例

## 说明

这个 Skill 适合从 0 创建服务端项目骨架，目标是先建立最小可运行服务壳子，而不是一次性铺满完整业务逻辑或复杂基础设施。

## 最小调用示例

```text
请使用 backend-service-scaffold skill，为当前项目创建服务端新项目骨架。

请先阅读：
1. 项目入口文档
2. skills/common/
3. 第一阶段目标
4. skills/backend-service-scaffold/scaffold-checklist.md
5. skills/backend-service-scaffold/default-stack.md

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
请使用 backend-service-scaffold skill，为当前需求从 0 起一个服务端项目骨架。

请先阅读：
1. 产品目标与第一阶段范围
2. 已确认的技术方案与接口契约
3. 项目入口文档和 skills/common/
4. 团队已知语言 / 框架 / 部署 / 日志 / 测试偏好
5. 是否需要数据库、缓存、消息队列、鉴权或第三方接入
6. skills/backend-service-scaffold/scaffold-checklist.md
7. skills/backend-service-scaffold/default-stack.md

请输出：
1. 当前启动判断
2. 推荐默认方案
3. 备选方案与取舍
4. 首批应创建的目录 / 模块 / 文件
5. 初始化步骤
6. 最小边界说明
7. 与 backend-development 的衔接方式
8. 本阶段不应提前做的事
9. 下一步建议 Skill
10. 验证方式
11. 未验证项
12. 风险点

要求：
- scaffold-checklist.md 和 default-stack.md 必须作为判断依据显式使用。
- 只创建最小可运行壳子，不要默认展开微服务拆分或复杂基础设施。
- 没有证据时，不要把语言、框架或平台偏好写成既定事实。
```

## 高约束调用示例

```text
请使用 backend-service-scaffold skill，严格为当前项目设计并创建服务端骨架方案。

必须先阅读：
1. 产品目标与第一阶段范围
2. 技术方案与接口契约
3. 项目入口文档和 skills/common/
4. 团队已知技术偏好
5. skills/backend-service-scaffold/scaffold-checklist.md
6. skills/backend-service-scaffold/default-stack.md

请严格按以下结构输出：
【当前启动判断】
【推荐默认方案】
【备选方案与取舍】
【首批应创建的目录 / 模块 / 文件】
【初始化步骤】
【最小边界说明】
【与 backend-development 的衔接方式】
【本阶段不应提前做的事】
【下一步建议 Skill】
【验证方式】
【未验证项】
【风险点】

要求：
- 这是 scaffold 层，不是完整业务实现层。
- 不要默认展开微服务拆分、复杂编排或完整基础设施接入。
- 无法验证的信息必须进入【未验证项】。
```

## 适用提醒

- 适合服务端项目还不存在时使用。
- 如果只是继续修改已有服务端项目，应切到 `backend-development`。
- 如果接口还没设计清楚，应先使用 `api-design`。
