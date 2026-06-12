# 使用示例

## 说明

这个 Skill 适合在线上问题已经有现象、日志、Crash 或发布记录时，系统性收集证据并定位根因，不靠猜。

## 最小调用示例

```text
请使用 bug-triage skill 定位这个线上问题。

已知信息：
1. 用户反馈或复现线索
2. Crash / 日志 / 发布记录 / 相关 commit
3. 配置变更信息

请输出：
1. 问题现象
2. 影响范围
3. 已确认事实
4. 根因假设
5. 证据
6. 止血方案
7. 修复方案
8. 回滚建议
9. 待补充信息

要求：
- 证据不足时不要编造根因。
- 生产数据只读。
```

## 推荐调用示例

```text
请使用 bug-triage skill，定位当前线上问题。

请先阅读：
1. 用户反馈和复现线索
2. Crash、日志、发布记录、相关 commit
3. 配置变更信息
4. skills/bug-triage/log-analysis.md
5. skills/bug-triage/incident-template.md

请输出：
1. 问题现象
2. 影响范围
3. 时间范围
4. 已确认事实
5. 根因假设
6. 证据
7. 止血方案
8. 修复方案
9. 回滚建议
10. 待补充信息

要求：
- 必须显式使用 log-analysis.md 和 incident-template.md。
- 先收集证据，再建立根因假设。
- 如果证据不足，明确指出还需要补哪些日志、Crash 或发布信息。
```

## 高约束调用示例

```text
请使用 bug-triage skill，严格定位当前线上问题。

必须先阅读：
1. 用户反馈与复现线索
2. Crash、日志、发布记录、相关 commit
3. 配置变更信息
4. skills/bug-triage/log-analysis.md
5. skills/bug-triage/incident-template.md

请严格按以下结构输出：
【问题现象】
【影响范围】
【时间范围】
【已确认事实】
【根因假设】
【证据】
【止血方案】
【修复方案】
【回滚建议】
【待补充信息】

要求：
- 证据不足时不允许编造根因。
- 生产数据只读。
- 高风险修复必须标记需要人工审批。
```

## 适用提醒

- 适合已经有异常现象和初步证据时使用。
- 如果只是监控层面发现异常但证据还很粗，应先用 `monitoring-analysis`。
- 如果已经进入事故止血阶段，应切到 `incident-response`。
