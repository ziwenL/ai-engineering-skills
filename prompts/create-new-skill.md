# Create New Skill Prompt

请根据本次会话中已经验证、可复用、长期有价值的流程，生成一个新的 Skill。

要求：

1. 放在 `.ai/ai-engineering-skills/skills/<skill-name>/SKILL.md`。
2. 必须包含 frontmatter：
   - name
   - description
3. 必须包含：
   - 适用场景
   - 输入
   - 工作流程
   - 输出格式
   - 约束
   - 不适用场景
4. 如果 Skill 目录下需要新增 `checklist.md`、`architecture.md`、`log-analysis.md` 等辅助文件，必须在 `SKILL.md` 的输入或工作流程中明确要求读取它们。
5. 开发类 Skill 要写清验证方式；审查类 Skill 要写清证据要求、风险分级和是否阻塞。
6. 不要写入密钥、Token、隐私、临时日志、未验证猜测。
