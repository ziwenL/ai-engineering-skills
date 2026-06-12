# 使用示例

## 说明

这个 Skill 适合在已有服务端项目中做接口开发、业务逻辑调整、兼容性修复或安全约束完善。示例强调先读检查清单、明确接口边界，再做最小实现并验证。

## 最小调用示例

```text
请使用 backend-development skill 实现该需求。

请先阅读：
1. 已确认的需求分析
2. 已确认的技术方案
3. 项目入口文档
4. skills/common/
5. skills/backend-development/api-checklist.md
6. skills/backend-development/security-checklist.md
7. 服务端相似接口或业务实现

要求：
- 先列出计划修改的文件和原因。
- 明确接口变化、错误处理和兼容性影响。
- 完成后运行相关测试或验证命令。

最后输出：
1. 修改摘要
2. 验证结果
3. 未验证项
4. 风险点
```

## 推荐调用示例

```text
请使用 backend-development skill 在当前服务端项目中实现这个需求。

请按以下顺序进行：
1. 阅读需求分析和技术方案
2. 阅读项目入口文档和 skills/common/
3. 阅读 skills/backend-development/api-checklist.md
4. 阅读 skills/backend-development/security-checklist.md
5. 查找项目中的相似接口、错误码和业务流程实现

实现要求：
1. 先列出计划修改的文件清单和原因
2. 明确请求链路、入参、出参、错误码和兼容边界
3. 检查鉴权、权限、幂等、限流、日志和监控影响
4. 不引入与当前需求无关的重构
5. 补齐必要测试，至少覆盖主流程和异常流程

完成后请输出：
1. 修改文件列表
2. 接口契约变化
3. 核心业务逻辑
4. 鉴权 / 权限 / 幂等 / 限流检查
5. 日志与监控影响
6. 测试与验证结果
7. 兼容性与回滚方案
8. 未验证项
9. 风险点
```

## 高约束调用示例

```text
请使用 backend-development skill 实现当前需求，并优先控制接口兼容性和线上风险。

必须先阅读：
1. 已确认的需求分析
2. 已确认的技术方案
3. 项目入口文档
4. skills/common/
5. skills/backend-development/api-checklist.md
6. skills/backend-development/security-checklist.md
7. 至少 1 个相似接口实现

执行要求：
- 先输出计划修改文件清单，不要直接开改。
- 不要修改生产配置或生产数据。
- 没有验证证据时，不要声称接口已可用。
- 无法确认的信息必须进入未验证项。

请严格按以下结构输出：
【修改文件列表】
【每个文件的修改原因】
【接口契约变化】
【核心业务逻辑】
【鉴权 / 权限 / 幂等 / 限流检查】
【日志与监控影响】
【测试与验证结果】
【兼容性与回滚方案】
【未验证项】
【风险点】
```

## 适用提醒

- 适合已有服务端项目内的接口与业务开发。
- 如果服务端项目尚未创建，应优先使用 `backend-service-scaffold`。
- 如果当前还处于接口契约设计阶段，应先用 `api-design`。
