# Skill Usage Examples Final Batch Design

## Goal

完成仓库剩余 Skill 的调用示例层收尾，让所有公开 Skill 都具备：

- `SKILL.md` 中的最小调用示例
- 独立的 `usage-examples.md`

本批次覆盖：

- `android-app-scaffold`
- `ios-app-scaffold`
- `data-model-design`
- `frontend-development`

## Why These Four Remain

前四批已经覆盖：

- 上下文、需求、方案、测试
- Android / iOS / Backend 开发
- 绿地起盘、API、scaffold、Android 到 iOS 复刻
- 线上问题、CI、审查、发布

剩下的 4 个分成两类：

1. 绿地客户端骨架层：
   - `android-app-scaffold`
   - `ios-app-scaffold`
2. 横向能力层：
   - `data-model-design`
   - `frontend-development`

补完这一批后，仓库将实现“全部 skill 都有示例层”的目标。

## Design Approach

继续沿用统一的双层结构：

```text
skills/<skill-name>/
├── SKILL.md
└── usage-examples.md
```

### `SKILL.md`

保留：

- 适用场景
- 输入
- 工作流程
- 输出格式
- 约束
- 不适用场景

并补上：

- `## 使用示例`
- 最小调用示例
- 指向 `usage-examples.md`

### `usage-examples.md`

统一结构：

```text
# 使用示例
## 说明
## 最小调用示例
## 推荐调用示例
## 高约束调用示例
## 适用提醒
```

## Special Focus

### Scaffold Skills

`android-app-scaffold` 和 `ios-app-scaffold` 的示例要强调：

- 这是起壳，不是直接展开完整业务实现
- 必须显式使用 `scaffold-checklist.md` 与 `default-stack.md`
- 输出要能自然衔接到 `android-development` / `ios-development`

### Data Model Design

`data-model-design` 的示例要强调：

- 实体、字段、映射、迁移、缓存和回滚一起考虑
- 没有验证路径时，不要把迁移说成低风险

### Frontend Development

`frontend-development` 的示例要强调：

- 先找相似页面和状态管理方式
- 不只做 happy path
- 要覆盖 loading / empty / error / success

## Success Criteria

本批次完成后，应满足：

1. 这 4 个 Skill 都有 `usage-examples.md`
2. 对应 `SKILL.md` 都有最小调用示例入口
3. `python scripts/check_skills.py` 全量通过
4. `skills/` 下除 `common` 外的所有 Skill 目录都具备 `usage-examples.md`
