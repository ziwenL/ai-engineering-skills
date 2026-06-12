# 使用示例

## 说明

这个 Skill 适合把一次成功会话或复盘结论，沉淀为新的 Skill 或对已有 Skill 的改进。重点是只沉淀已验证、可复用、长期有效的内容。

## 最小调用示例

```text
请使用 skill-authoring skill，根据刚才 session-retrospective 的结论，生成或改进 Skill。

请输出：
1. 建议修改位置
2. 修改原因
3. 主文件 patch
4. 辅助文件 patch
5. 风险
6. 是否需要同步修改 common 或入口文件

要求：
- 只沉淀已验证、可复用、长期有效的内容。
- 不要写入密钥、隐私、临时日志或未经验证的猜测。
```

## 推荐调用示例

```text
请使用 skill-authoring skill，把这次任务中已经验证有效的经验沉淀为 Skill 改动。

请基于以下输入：
1. session-retrospective 输出
2. 本次已验证的会话经验
3. 目标 Skill 或待新增 Skill 的定位
4. 如有需要，一并规划 checklist、architecture、log-analysis 等辅助文件

请输出：
1. 建议修改位置
2. 修改原因
3. 主文件 patch
4. 辅助文件 patch
5. 风险
6. 是否需要同步修改 common 或入口文件

要求：
- 判断是更新 common、更新已有 Skill，还是新增 Skill。
- 只沉淀已验证、可复用、长期有效的内容。
- 如果需要辅助文件，必须说明它们与 `SKILL.md` 的关系。
```

## 高约束调用示例

```text
请使用 skill-authoring skill，把当前复盘结论沉淀为 Skill 改动建议。

请严格按以下结构输出：
【建议修改位置】
【修改原因】
【主文件 patch】
【辅助文件 patch】
【风险】
【是否需要同步修改 common 或入口文件】

要求：
- 只沉淀已验证、可复用、长期有效的内容。
- 不要写入密钥、Token、隐私、临时日志或未经验证的猜测。
- 如果主文件依赖辅助文件，必须保证 `SKILL.md` 显式引用它们。
```

## 适用提醒

- 适合在 `session-retrospective` 之后使用。
- 如果只是一次性经验、还未验证是否可复用，不适合直接写成 Skill。
- 完成后通常还应再用 `code-review` 检查 Skill 本身质量。
