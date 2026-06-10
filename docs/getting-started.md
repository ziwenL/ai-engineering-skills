# Getting Started

本文件是 README 的简化落地版。完整说明请阅读仓库根目录 `README.md`。

## 1. 业务项目添加 Submodule

```powershell
cd C:\Users\<your-username>\Projects\your-business-project
git submodule add https://github.com/<your-org-or-username>/ai-engineering-skills.git .ai/ai-engineering-skills
git submodule update --init --recursive
python .ai\ai-engineering-skills\scripts\init_submodule_project.py .
git add .gitmodules .ai/ai-engineering-skills CLAUDE.md AGENTS.md docs
git commit -m "add ai engineering skills"
```

## 输出验收标准

```text
CLAUDE.md 存在
AGENTS.md 存在
.ai/ai-engineering-skills/skills 存在
docs/decisions 存在
docs/incident-history 存在
docs/ai-sessions 存在
git submodule status 正常
```

## 你需要人工做的事

```text
确认路径正确
确认仓库权限正确
确认入口文件没有覆盖已有规则
确认业务特有规则写在业务项目入口文件，而不是公共 Skill
```

## 2. 第一次让 AI 理解项目

```text
请使用 context-bootstrap skill，为当前项目建立 AI Coding 上下文。
不要修改代码，只输出项目技术栈、主要模块、构建测试方式、适用 Skill、开发约束和缺失上下文。
```

## 输出验收标准

```text
项目技术栈
主要模块结构
构建命令
测试命令
适用 Skill
缺失上下文
```

## 你需要人工做的事

```text
检查 AI 是否误判项目
补充长期有效的项目规则
不要让 AI 在这一步修改代码
```

## 3. 第一周固定工作流

```text
requirement-analysis
→ technical-design
→ test-case-generation
→ development
→ code-review
→ session-retrospective
```

每一步都需要检查输出是否符合 README 中的验收标准。
