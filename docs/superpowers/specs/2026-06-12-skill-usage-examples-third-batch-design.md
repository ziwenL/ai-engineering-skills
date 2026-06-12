# Skill Usage Examples Third Batch Design

## Goal

继续为仓库补齐 Skill 的调用示例层，这一批聚焦于：

- 绿地起盘分流
- Android 到 iOS 的复制链路
- 接口设计
- 后端新项目 scaffold

本批次覆盖：

- `android-to-ios-bootstrap`
- `android-to-ios-porting`
- `greenfield-bootstrap`
- `api-design`
- `backend-service-scaffold`

## Why This Batch

前两批已经补齐了：

- 上下文建立
- 需求分析
- 技术方案
- 测试用例
- Android / iOS / Backend 实现
- 代码审查
- 会话复盘与 Skill 沉淀

第三批补的是两条“结构性流程”：

1. 从 0 起盘的多端分流链路
2. Android 已有实现时向 iOS 复制的链路

同时补齐这两条链路中最关键的两个中间 Skill：

- `api-design`
- `backend-service-scaffold`

这样仓库的高频用户路径会更完整：

- 已有项目开发路径
- 新项目起盘路径
- Android 到 iOS 复刻路径

## Design Approach

继续沿用已经验证通过的双层结构：

```text
skills/<skill-name>/
├── SKILL.md
└── usage-examples.md
```

`SKILL.md` 放：

- Skill 作用定义
- 输入 / 工作流程 / 输出 / 约束
- 一个最小调用示例

`usage-examples.md` 放：

- 更完整的多场景可复制提示词

## Writing Focus

这批示例相比前两批，需要额外强调：

### 1. 分流判断

不是直接让 AI 开始干，而是先判断当前任务应该进入哪条链路。

### 2. 阶段边界

例如：

- `greenfield-bootstrap` 不负责直接大规模生成实现
- `android-to-ios-bootstrap` 不负责直接写完整 iOS 代码
- `api-design` 不负责直接进入服务端实现
- `backend-service-scaffold` 不等同于 `backend-development`

### 3. 未验证项

这批 Skill 很多都处于“设计 / 路由 / scaffold”边界，天然容易出现假设，因此示例词里必须继续强调：

- 不要把猜测写成事实
- 缺少依据时写入“未验证项”

## Success Criteria

本批次完成后，应满足：

1. 上述 5 个 Skill 都有 `usage-examples.md`
2. 对应 `SKILL.md` 都有最小调用示例入口
3. 所有辅助文件都被显式引用
4. `python scripts/check_skills.py` 继续全量通过
