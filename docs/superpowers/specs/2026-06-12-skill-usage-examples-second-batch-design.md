# Skill Usage Examples Second Batch Design

## Goal

在第一批“上下文与开发类” Skill 完成调用示例层之后，继续覆盖一批更贴近日常主流程的 Skill，让用户从需求分析到审查沉淀的整条链路，都能直接复制高质量提示词。

本批次覆盖：

- `requirement-analysis`
- `test-case-generation`
- `code-review`
- `session-retrospective`
- `skill-authoring`

## Why This Batch

这 5 个 Skill 共同构成了一个高频闭环：

1. `requirement-analysis` 负责把原始需求拆清楚
2. `technical-design` 负责方案设计
3. `test-case-generation` 负责测试覆盖设计
4. `code-review` 负责实现后的风险审查
5. `session-retrospective` 与 `skill-authoring` 负责把经验继续沉淀回仓库

第一批已经补了：

- `context-bootstrap`
- `technical-design`
- `android-development`
- `ios-development`
- `backend-development`

因此第二批最合理的补位，就是把“开发前后”的分析、审查和沉淀链路补完整。

## Design Approach

继续沿用已经验证通过的双层结构：

```text
skills/<skill-name>/
├── SKILL.md
└── usage-examples.md
```

### `SKILL.md`

保留 Skill 的职责定义、流程、输出和约束，并新增：

- `## 使用示例`
- 一个最小调用示例
- “更多示例见 `usage-examples.md`”

### `usage-examples.md`

每个 Skill 统一包含：

```text
# 使用示例
## 说明
## 最小调用示例
## 推荐调用示例
## 高约束调用示例
## 适用提醒
```

## Batch Characteristics

相比第一批，这一批有两个差异：

### 1. 更偏“前后置工作流”

第一批偏执行期：

- 建立上下文
- 做方案
- 写 Android / iOS / Backend 代码

第二批偏执行前后：

- 分析需求
- 补测试思路
- 做代码审查
- 复盘沉淀经验

### 2. 其中包含审查类与沉淀类 Skill

所以示例提示词里要更强调：

- 不要直接进入实现
- 明确证据、风险、阻塞判断
- 只沉淀已验证、可复用、长期有效的信息

## Success Criteria

本批次完成后，应满足：

1. 上述 5 个 Skill 都有 `usage-examples.md`
2. 对应 `SKILL.md` 都带有最小调用示例入口
3. 所有新增支持文件都被 `SKILL.md` 显式引用
4. `python scripts/check_skills.py` 继续全量通过
