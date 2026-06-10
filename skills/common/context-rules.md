# 上下文规则

## 新会话启动

AI 必须先读取：

1. 当前工具入口文件：
   - Claude Code：`CLAUDE.md`
   - Codex：`AGENTS.md`
2. `.ai/ai-engineering-skills/skills/common/`
3. 与当前任务相关的 Skill
4. 项目中已有相关文档和相似实现

## 上下文不足时

不要猜测。必须输出：

```text
【上下文不足】
【需要补充的信息】
【建议读取的文件】
【暂不能确认的判断】
```

## 会话结束

每次任务完成后，必须执行 `session-retrospective`，判断是否需要沉淀。
