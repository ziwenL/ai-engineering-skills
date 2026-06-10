# Migrate Claude Skills To Agent Neutral Prompt

请把 Claude 专属结构迁移为模型无关结构。

原则：

1. 核心 Skills 放入 `skills/`。
2. Claude 专属内容放入 `adapters/claude/`。
3. Codex 入口放入 `adapters/codex/`。
4. Cursor 入口放入 `adapters/cursor/`。
5. 不丢失原有 Skill 语义。
