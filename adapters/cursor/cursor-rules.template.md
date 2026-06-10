# Cursor Rules

本项目使用：

```text
.ai/ai-engineering-skills/skills/
```

作为 AI Coding Skills 来源。

规则：

1. 先读取 common。
2. 根据任务读取对应 Skill；如果同目录还有 `checklist.md`、`architecture.md`、`log-analysis.md` 等辅助文件，也要继续读取。
   如果是“Android 已有实现，需要同步到 iOS”，优先读取 `android-to-ios-bootstrap`，再决定是否进入 `android-to-ios-porting` 或 `ios-development`。
3. 先分析，再设计，再实现。
4. 开发类 Skill 输出时要写清验证方式、验证结果、未验证项。
5. 审查类 Skill 输出时要写清证据、风险等级、是否阻塞。
6. 不修改无关文件。
7. 不做无关重构。
8. 任务结束执行 session-retrospective。
