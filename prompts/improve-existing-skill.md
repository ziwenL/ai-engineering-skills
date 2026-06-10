# Improve Existing Skill Prompt

请基于本次会话反馈，改进已有 Skill。

请输出：

1. 需要修改的 Skill
2. 修改原因
3. 建议 patch
4. 风险
5. 是否需要同步修改 common 或入口文件
6. 是否需要补充或引用同目录下的辅助文件

改进要求：

- 目标 Skill 应尽量补齐：适用场景、输入、工作流程、输出格式、约束、不适用场景
- 如果当前 Skill 只有检查项或简短流程，需要改成可执行步骤
- 如果存在 `checklist.md`、`architecture.md`、`log-analysis.md` 等辅助文件，主 `SKILL.md` 不能与它们失联
