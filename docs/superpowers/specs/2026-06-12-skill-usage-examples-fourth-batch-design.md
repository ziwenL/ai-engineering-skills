# Skill Usage Examples Fourth Batch Design

## Goal

继续为仓库补齐 Skill 的调用示例层，这一批聚焦“线上问题与发布审查链”。

本批次覆盖：

- `monitoring-analysis`
- `bug-triage`
- `incident-response`
- `postmortem`
- `build-ci-fix`
- `security-review`
- `performance-review`
- `release-check`

## Why This Batch

前面三批已经补了：

- 上下文建立、需求分析、技术方案、测试用例
- Android / iOS / Backend 开发
- 绿地起盘、API 设计、scaffold、Android 到 iOS 复刻
- 代码审查、会话复盘和 Skill 沉淀

当前还缺少的是“出问题后怎么办”和“上线前怎么做审查”这条链路。

这一批补完后，仓库将具备更完整的闭环：

1. 监控发现异常
2. Bug 定位
3. 事故应急
4. 事故复盘
5. CI 修复
6. 安全审查
7. 性能审查
8. 发布检查

## Design Approach

继续沿用已经验证通过的双层结构：

```text
skills/<skill-name>/
├── SKILL.md
└── usage-examples.md
```

### `SKILL.md`

放：

- Skill 的职责和边界
- 输入 / 工作流程 / 输出格式 / 约束
- 一个最小调用示例
- 指向 `usage-examples.md` 的入口

### `usage-examples.md`

统一包含：

```text
# 使用示例
## 说明
## 最小调用示例
## 推荐调用示例
## 高约束调用示例
## 适用提醒
```

## Writing Focus

这一批示例需要额外强调：

### 1. 证据优先

线上问题、审查和发布判断都不能凭感觉下结论。示例提示词里要继续强化：

- 区分事实和假设
- 证据不足时写成待确认 / 未验证项

### 2. 不越权

例如：

- `incident-response` 不等于自动执行高风险操作
- `build-ci-fix` 不等于删测试、降规则
- `release-check` 不等于为了上线而隐藏阻塞问题

### 3. 阶段边界

不同 Skill 负责不同阶段：

- `monitoring-analysis` 负责看异常轮廓
- `bug-triage` 负责收集证据和定位问题
- `incident-response` 负责止血与协调
- `postmortem` 负责复盘与长期防线

## Success Criteria

本批次完成后，应满足：

1. 上述 8 个 Skill 都有 `usage-examples.md`
2. 对应 `SKILL.md` 都有最小调用示例入口
3. 所有辅助文件都被 `SKILL.md` 显式引用
4. `python scripts/check_skills.py` 继续全量通过
