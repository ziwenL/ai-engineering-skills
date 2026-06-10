# AI Engineering Skills

这是一个 **模型无关、工具可替换** 的 AI Coding 工程化 Skills 仓库模板。

它不是一组一次性 Prompt，而是把团队的软件研发流程沉淀为：

- 可复用的 AI Skills
- 可版本管理的工程规则
- 可审计的开发流程
- 可持续迭代的上下文资产
- 可适配 Claude Code / Codex / Cursor / 其他 Coding Agent 的工程知识库

推荐通过 **Git Submodule** 引入到业务项目中，让多个业务项目共享同一套 AI Engineering Skills。

---

## 一、这个项目解决什么问题

普通 AI Coding 经常遇到的问题是：

```text
AI 每次新会话都不了解项目
AI 容易跳过需求分析直接写代码
AI 容易大范围重构
AI 容易遗漏测试、异常态、边界条件
AI 修完问题后经验没有沉淀
换一个工具后原来的规则不能复用
```

本仓库的目标是把 AI Coding 从“临时聊天”变成“流程化工程系统”：

```text
上下文初始化
→ 需求分析
→ 技术方案
→ 测试用例
→ 功能开发
→ Code Review
→ 安全 / 性能 / CI 检查
→ 发版检查
→ 监控分析
→ Bug 定位
→ 事故应急
→ 事故复盘
→ 会话沉淀
→ Skill 迭代
```

---

## 二、设计原则

### 1. 模型无关

核心能力放在：

```text
skills/
```

Claude、Codex、Cursor 等不同工具只通过 `adapters/` 适配，不把核心流程绑定到某个工具。

### 2. 工具可替换

```text
Claude Code 读取 CLAUDE.md
Codex 读取 AGENTS.md
Cursor 读取 cursor rules
其他 Agent 读取通用入口文件
```

### 3. Submodule 优先

业务项目通过 Git Submodule 引入本仓库：

```text
your-project/.ai/ai-engineering-skills/
```

这样多个项目可以共享同一套 Skills，并通过 Git 版本管理持续迭代。

### 4. 每次任务后沉淀

每次 AI Coding 任务结束都必须问：

```text
本次会话有没有值得提取成 common？
有没有需要更新某个 Skill？
有没有需要新增 Skill？
有没有需要写入 CLAUDE.md / AGENTS.md / docs？
```

---

## 三、仓库结构

```text
ai-engineering-skills/
├── README.md
├── skills/                                  # 核心长期资产：模型无关 Skills
│   ├── common/                              # 跨 Skill 复用规则
│   │   ├── engineering-principles.md
│   │   ├── security-rules.md
│   │   ├── context-rules.md
│   │   ├── output-format.md
│   │   └── risk-level.md
│   │
│   ├── context-bootstrap/                   # 新项目 / 新会话上下文初始化
│   ├── requirement-analysis/                # 需求分析
│   ├── technical-design/                    # 技术方案
│   ├── api-design/                          # 接口设计
│   ├── data-model-design/                   # 数据结构 / 数据库 / DTO 设计
│   │
│   ├── android-development/                 # Android 开发
│   ├── ios-development/                     # iOS 开发
│   ├── android-to-ios-porting/              # Android 到 iOS 复刻
│   ├── backend-development/                 # 服务端开发
│   ├── frontend-development/                # Web / H5 / 管理后台开发
│   │
│   ├── test-case-generation/                # 测试用例生成
│   ├── code-review/                         # 代码审查
│   ├── security-review/                     # 安全审查
│   ├── performance-review/                  # 性能审查
│   ├── build-ci-fix/                        # 构建 / CI 失败修复
│   │
│   ├── bug-triage/                          # 线上 Bug 定位
│   ├── release-check/                       # 发版检查
│   ├── monitoring-analysis/                 # 监控分析
│   ├── incident-response/                   # 线上事故应急处理
│   ├── postmortem/                          # 事故复盘
│   │
│   ├── session-retrospective/               # 会话沉淀
│   └── skill-authoring/                     # 用 AI 生成 / 迭代 Skill
│
├── adapters/                                # 工具适配层
│   ├── claude/                              # Claude Code 入口模板
│   ├── codex/                               # Codex 入口模板
│   ├── cursor/                              # Cursor rules 模板
│   └── generic/                             # 通用 Agent 模板
│
├── templates/                               # 输出模板
├── prompts/                                 # 用 AI 生成 / 迭代 Skill 的提示词
├── scripts/                                 # 安装、检查、初始化脚本
└── docs/                                    # 仓库自身说明
```

---

## 四、快速开始：用 Git Submodule 接入业务项目

下面以 Windows PowerShell 为主，因为它最容易踩路径和兼容性问题。Git Bash / macOS / Linux 可参考同等命令。

---

### 第 1 步：准备 AI Engineering Skills 仓库

如果你是第一次使用，先把本仓库推到 GitHub。

```powershell
cd C:\Users\<your-username>\Projects\ai-engineering-skills

git init
git add .
git commit -m "init ai engineering skills"

git remote add origin https://github.com/<your-org-or-username>/ai-engineering-skills.git
git push -u origin main
```

#### 输出验收标准

执行成功后，应该满足：

```text
1. GitHub 上能看到 ai-engineering-skills 仓库。
2. 仓库根目录包含 README.md、skills、adapters、templates、prompts、scripts、docs。
3. 本地执行 git status 显示工作区干净。
```

可检查：

```powershell
git status
git remote -v
```

#### 你需要人工做的事

```text
1. 确认远程仓库地址是否正确。
2. 确认仓库是 public 还是 private。
3. 如果是 private，确认业务项目所在环境有权限拉取 submodule。
4. 确认不要把业务项目代码、密钥、Token 提交到这个公共 Skills 仓库。
```

---

### 第 2 步：进入业务项目并确认 Git 状态

假设你的业务项目是：

```text
C:\Users\<your-username>\Projects\your-business-project
```

进入业务项目：

```powershell
cd C:\Users\<your-username>\Projects\your-business-project
```

检查是否已经是 Git 仓库：

```powershell
git status
```

如果提示：

```text
fatal: not a git repository
```

说明业务项目还没有初始化 Git，需要执行：

```powershell
git init
git add .
git commit -m "init project"
```

#### 输出验收标准

执行成功后，应该满足：

```text
1. 业务项目根目录存在 .git。
2. git status 不再提示 fatal。
3. 至少有一次初始 commit。
```

#### 你需要人工做的事

```text
1. 确认当前目录真的是业务项目根目录，而不是上级目录或子目录。
2. 确认 .gitignore 已经排除 build、.gradle、local.properties、node_modules、Pods 等不应提交的文件。
3. 如果项目已经有远程仓库，不要重复 git init 到错误目录。
4. 如果项目还不想纳入 Git，暂时不要使用 submodule，先使用复制安装方式。
```

---

### 第 3 步：添加 ai-engineering-skills 为 Submodule

创建 `.ai` 目录：

```powershell
New-Item -ItemType Directory -Force .ai
```

添加 submodule：

```powershell
git submodule add https://github.com/<your-org-or-username>/ai-engineering-skills.git .ai/ai-engineering-skills
git submodule update --init --recursive
```

#### 输出验收标准

执行成功后，业务项目中应该出现：

```text
.gitmodules
.ai/
└── ai-engineering-skills/
    ├── README.md
    ├── skills/
    ├── adapters/
    ├── templates/
    ├── prompts/
    ├── scripts/
    └── docs/
```

可以检查：

```powershell
Get-ChildItem .ai\ai-engineering-skills
Get-Content .gitmodules
git submodule status
```

#### 你需要人工做的事

```text
1. 确认 submodule 路径是 .ai/ai-engineering-skills，不要放到 .ai/skills。
2. 确认 .gitmodules 里的 URL 是你的真实仓库地址。
3. 如果提示路径已存在，先确认旧目录是否需要备份。
4. 如果仓库是 private，确认当前 Git 凭据有权限 clone。
```

#### 常见错误处理

如果提示：

```text
fatal: '.ai/ai-engineering-skills' already exists and is not a valid git repo
```

说明该目录已存在但不是 submodule。可以备份：

```powershell
Rename-Item .ai\ai-engineering-skills ai-engineering-skills_backup
git submodule add https://github.com/<your-org-or-username>/ai-engineering-skills.git .ai/ai-engineering-skills
```

如果确认旧目录不要了，可以删除：

```powershell
Remove-Item -Recurse -Force .ai\ai-engineering-skills
git submodule add https://github.com/<your-org-or-username>/ai-engineering-skills.git .ai/ai-engineering-skills
```

---

### 第 4 步：初始化业务项目入口文件

业务项目根目录需要两个入口文件：

```text
CLAUDE.md    # Claude Code 读取
AGENTS.md    # Codex 读取
```

可以手动复制：

```powershell
Copy-Item .ai\ai-engineering-skills\adapters\claude\CLAUDE.md.template .\CLAUDE.md
Copy-Item .ai\ai-engineering-skills\adapters\codex\AGENTS.md.template .\AGENTS.md
```

也可以执行脚本：

```powershell
python .ai\ai-engineering-skills\scripts\init_submodule_project.py .
```

该脚本会自动创建：

```text
CLAUDE.md
AGENTS.md
docs/decisions
docs/incident-history
docs/ai-sessions
```

#### 输出验收标准

业务项目根目录应该出现：

```text
CLAUDE.md
AGENTS.md
docs/
├── decisions/
├── incident-history/
└── ai-sessions/
```

并且 `CLAUDE.md` / `AGENTS.md` 中应该引用：

```text
.ai/ai-engineering-skills/skills/
```

可以检查：

```powershell
Get-Content .\CLAUDE.md
Get-Content .\AGENTS.md
```

#### 你需要人工做的事

```text
1. 确认 CLAUDE.md 和 AGENTS.md 没有覆盖你已有的重要项目说明。
2. 如果项目已有 CLAUDE.md，需要手动合并，不要直接覆盖。
3. 把项目特有规则写到业务项目根目录的 CLAUDE.md / AGENTS.md，而不是写回公共 Skills 仓库。
4. 确认 docs 目录可以提交到业务项目仓库。
```

---

### 第 5 步：提交业务项目中的接入变更

执行：

```powershell
git add .gitmodules .ai/ai-engineering-skills CLAUDE.md AGENTS.md docs
git commit -m "add ai engineering skills"
```

#### 输出验收标准

执行成功后：

```text
1. git status 显示工作区干净。
2. git submodule status 能看到 ai-engineering-skills 的 commit hash。
3. 业务项目仓库记录了 .gitmodules 和 submodule 指针。
```

检查：

```powershell
git status
git submodule status
```

#### 你需要人工做的事

```text
1. 确认提交内容里没有把整个 submodule 内容复制进业务仓库。
2. 确认提交的是 submodule 指针，而不是普通文件夹。
3. 确认 CLAUDE.md / AGENTS.md 里的路径正确。
4. 如果团队协作，需要告诉其他人 clone 时使用 --recurse-submodules。
```

---

## 五、克隆已有业务项目时如何拉取 Submodule

如果团队其他成员 clone 业务项目，推荐：

```powershell
git clone --recurse-submodules <your-business-project-url>
```

如果已经 clone 了，但 submodule 为空：

```powershell
git submodule update --init --recursive
```

#### 输出验收标准

```text
1. .ai/ai-engineering-skills 目录不为空。
2. .ai/ai-engineering-skills/skills 存在。
3. CLAUDE.md / AGENTS.md 能引用到正确路径。
```

#### 你需要人工做的事

```text
1. 如果 clone 失败，检查 submodule 仓库权限。
2. 如果 submodule 目录为空，执行 git submodule update --init --recursive。
3. 如果团队使用私有仓库，确认每个成员都配置了 GitHub 凭据。
```

---

## 六、更新 Skills

当 `ai-engineering-skills` 仓库更新后，在业务项目中执行：

```powershell
git submodule update --remote .ai/ai-engineering-skills

git add .ai/ai-engineering-skills
git commit -m "update ai engineering skills"
```

#### 输出验收标准

```text
1. git submodule status 显示新的 commit hash。
2. 业务项目产生一条更新 submodule 指针的 commit。
3. .ai/ai-engineering-skills/README.md、skills 等内容为最新版本。
```

#### 你需要人工做的事

```text
1. 更新前先确认本次 Skills 改动是否适合当前业务项目。
2. 更新后让 AI 检查 CLAUDE.md / AGENTS.md 是否仍然兼容。
3. 如果 Skills 有破坏性改动，需要通知团队。
4. 不要在业务项目里直接修改 submodule 内容后忘记提交到 Skills 仓库。
```

---

## 七、Claude Code 使用方法

在 Claude Code 中打开业务项目根目录。

### 第 0 步：让 AI 先理解当前项目

输入：

```text
请使用 context-bootstrap skill，为当前项目建立 AI Coding 上下文。

请先阅读：
1. CLAUDE.md
2. .ai/ai-engineering-skills/skills/common/
3. README
4. 主要目录结构
5. 构建脚本
6. 核心架构代码
7. 测试/CI 配置

然后输出：
1. 项目技术栈判断
2. 项目主要模块结构
3. 适合使用哪些 Skill
4. 当前项目开发约束
5. 还缺少哪些上下文文档

要求：
- 不要修改代码。
- 不要猜测无法从代码确认的信息。
- 如果上下文不足，请明确列出需要补充的文件或信息。
```

#### 输出验收标准

AI 的输出应该至少包含：

```text
1. 项目技术栈，例如 Android / iOS / Backend / Web。
2. 主要模块结构。
3. 构建命令和测试命令。
4. 当前可用 Skill 列表。
5. 项目开发约束。
6. 缺失上下文清单。
```

#### 你需要人工做的事

```text
1. 检查 AI 是否误判技术栈。
2. 检查 AI 是否遗漏关键模块。
3. 补充 AI 不知道的构建命令、发版流程、测试方式。
4. 把长期有效的项目规则写入 CLAUDE.md。
5. 不要让 AI 在这一步修改业务代码。
```

---

## 八、Codex 使用方法

在 Codex 中打开业务项目根目录。

### 第 0 步：让 AI 先理解当前项目

输入：

```text
请使用 context-bootstrap skill，为当前项目建立 AI Coding 上下文。

请先阅读：
1. AGENTS.md
2. CLAUDE.md，如果存在
3. .ai/ai-engineering-skills/skills/common/
4. README
5. 主要目录结构
6. 构建脚本
7. 核心架构代码
8. 测试/CI 配置

然后输出：
1. 项目技术栈判断
2. 项目主要模块结构
3. 适合使用哪些 Skill
4. 当前项目开发约束
5. 还缺少哪些上下文文档

要求：
- 不要修改代码。
- 不要猜测无法从代码确认的信息。
- 如果上下文不足，请明确列出需要补充的文件或信息。
```

#### 输出验收标准

AI 的输出应该至少包含：

```text
1. 已读取 AGENTS.md。
2. 已读取 common 规则。
3. 已识别项目技术栈和主要目录。
4. 已列出适用 Skill。
5. 已列出缺失上下文。
```

#### 你需要人工做的事

```text
1. 确认 Codex 是否按 AGENTS.md 的路径读取了 Skills。
2. 如果 Codex 没有自动读取 Skill，明确要求它读取对应 SKILL.md。
3. 把 Codex 适配过程中发现的问题更新到 AGENTS.md。
4. 不要把 Codex 特有的临时行为写入公共 Skill，除非它对其他 Agent 也适用。
```

---

## 九、第一周推荐工作流

第一周不要急着接飞书、生产日志、生产数据库或自动发版。

推荐只跑通：

```text
context-bootstrap
→ requirement-analysis
→ technical-design
→ test-case-generation
→ development
→ code-review
→ session-retrospective
```

---

### 第 1 步：使用 `requirement-analysis` 做需求分析

当你有一个新需求时，不要直接让 AI 写代码。先让它分析需求。

#### 输入方式

```text
请使用 requirement-analysis skill 分析以下需求。

需求内容：
【在这里粘贴需求】

请输出：
1. 业务目标
2. 用户故事
3. 主流程
4. 异常流程
5. 边界条件
6. 依赖模块
7. 待确认问题
8. 初步风险点

要求：
- 不要写代码。
- 不要直接给技术方案。
- 对无法确认的信息标记为“待确认”，不要猜。
```

#### 输出验收标准

AI 的输出应该至少包含：

```text
业务目标
用户故事
主流程
异常流程
边界条件
涉及模块
待确认问题
初步风险
```

#### 你需要人工做的事

```text
1. 检查 AI 是否误解需求。
2. 检查是否遗漏边界条件。
3. 检查是否把未确认内容当成事实。
4. 补充产品验收标准。
5. 对待确认问题给出答案，或者标记为后续确认。
```

---

### 第 2 步：使用 `technical-design` 生成技术方案

需求分析确认后，再进入技术方案。

#### 输入方式

```text
请基于已确认的需求分析，使用 technical-design skill 生成技术方案。

请输出：
1. 总体实现思路
2. 涉及模块
3. 修改文件清单
4. 数据结构变化
5. 接口变化
6. 状态流转
7. 错误处理
8. 测试方案
9. 风险点
10. 回滚或兼容方案

要求：
- 不要立即修改代码。
- 先查找项目中相似实现。
- 明确哪些是事实，哪些是假设。
```

#### 输出验收标准

技术方案应该回答清楚：

```text
改哪里
为什么这么改
怎么验证
有什么风险
是否影响旧功能
是否需要服务端配合
是否需要多端同步
是否需要测试补充
```

#### 你需要人工做的事

```text
1. 检查方案是否符合项目架构。
2. 检查改动范围是否过大。
3. 检查是否引入不必要的新依赖。
4. 检查是否遗漏错误处理和测试。
5. 确认是否需要服务端、Android、iOS、Web 多端同步。
6. 如果方案过大，要求 AI 重新生成最小可行方案。
```

---

### 第 3 步：使用 `test-case-generation` 生成测试用例

#### 输入方式

```text
请使用 test-case-generation skill，基于需求分析和技术方案生成测试用例。

请覆盖：
1. 正向用例
2. 异常用例
3. 边界用例
4. 兼容性用例
5. 回归用例
6. 自动化建议
7. 人工验证建议
```

#### 输出验收标准

测试用例应该覆盖：

```text
主流程
异常流程
边界输入
网络异常
权限异常
兼容性场景
旧功能回归
人工验证路径
自动化建议
```

#### 你需要人工做的事

```text
1. 检查是否遗漏真实用户场景。
2. 检查是否只覆盖 happy path。
3. 补充设备、系统版本、网络、账号状态等测试维度。
4. 判断哪些测试必须自动化，哪些可以人工验证。
5. 将关键用例同步给测试同学。
```

---

### 第 4 步：使用开发 Skill 做功能实现

根据项目类型选择一个开发 Skill：

```text
Android 项目：android-development
iOS 项目：ios-development
服务端项目：backend-development
Web / H5 / 管理后台：frontend-development
```

#### Android 输入示例

```text
请使用 android-development skill 实现该需求。

要求：
1. 先列出计划修改文件和原因。
2. 不修改与需求无关的代码。
3. 遵守当前项目架构。
4. 不引入新依赖，除非先征求确认。
5. 实现 loading、empty、error、success 等必要状态。
6. 实现后运行相关编译或测试命令。
7. 最后输出修改摘要、测试结果和风险点。
```

#### iOS 输入示例

```text
请使用 ios-development skill 实现该需求。

要求：
1. 先查找 iOS 项目中的相似实现。
2. 遵守当前项目架构。
3. 保持与 Android 或产品要求一致。
4. 明确状态处理、错误处理和空状态。
5. 不做无关重构。
6. 实现后说明验证方式。
```

#### 服务端输入示例

```text
请使用 backend-development skill 实现该需求。

要求：
1. 遵守当前服务端分层结构。
2. 明确接口入参、出参和错误码。
3. 不修改生产配置。
4. 不引入不必要的新依赖。
5. 补充必要测试。
6. 说明兼容性、回滚方式和风险点。
```

#### 输出验收标准

AI 实现后应该输出：

```text
修改文件列表
每个文件的修改原因
核心实现逻辑
测试 / 编译结果
无法测试的原因
潜在风险
人工验证步骤
```

#### 你需要人工做的事

```text
1. 检查是否修改了无关文件。
2. 检查是否破坏现有架构。
3. 检查是否遗漏 loading / empty / error / success。
4. 检查是否遗漏权限、网络、超时、异常返回。
5. 检查 AI 是否真的运行了测试，而不是口头声明。
6. 对高风险模块进行人工 Review。
```

---

### 第 5 步：使用 `code-review` 审查改动

#### 输入方式

```text
请使用 code-review skill 审查本次改动。

请重点检查：
1. 是否满足需求
2. 是否符合技术方案
3. 是否修改无关文件
4. 是否破坏现有架构
5. 是否遗漏异常和边界条件
6. 是否有测试缺口
7. 是否有安全或性能风险
```

#### 输出验收标准

Review 输出应该包含：

```text
结论：通过 / 有条件通过 / 不建议合并
主要问题
次要问题
测试缺口
风险点
建议修改
```

#### 你需要人工做的事

```text
1. 不要因为 AI 说通过就直接合并。
2. 重点看核心业务逻辑和边界条件。
3. 对安全、支付、权限、登录相关改动进行人工复核。
4. 如果 AI 指出问题，要求它给出最小修改方案。
5. 确认测试是否真实执行。
```

---

### 第 6 步：使用 `session-retrospective` 做会话复盘

每次任务结束后，都要让 AI 判断这次会话有没有值得沉淀的内容。

#### 输入方式

```text
请使用 session-retrospective skill，回顾本次会话。

请判断是否有内容值得沉淀到：
1. .ai/ai-engineering-skills/skills/common/
2. 某个已有 Skill
3. 新增 Skill
4. CLAUDE.md
5. AGENTS.md
6. docs/decisions/
7. docs/incident-history/
8. docs/ai-sessions/

请输出：
1. 建议沉淀内容
2. 推荐沉淀位置
3. 沉淀理由
4. 不应沉淀内容及原因
5. 如果需要修改文件，请给出具体 patch 或完整文件内容

要求：
- 只沉淀可复用、已验证、长期有价值的信息。
- 不沉淀隐私、密钥、临时日志、一次性数据。
- 不沉淀未经验证的猜测。
```

#### 输出验收标准

AI 的复盘结果应该分清：

```text
通用规则 → skills/common/
流程变化 → 某个已有 Skill
新流程 → 新增 Skill
项目特定约束 → CLAUDE.md / AGENTS.md
技术决策 → docs/decisions/
事故经验 → docs/incident-history/
会话摘要 → docs/ai-sessions/
```

#### 你需要人工做的事

```text
1. 判断这个经验下次是否还会用到。
2. 判断它是通用规则，还是项目特有规则。
3. 判断是否已经被验证。
4. 检查是否包含敏感信息。
5. 决定是否允许 AI 修改 Skill 或 common。
6. 如果修改公共 Skills 仓库，要单独提交并 Review。
```

---

### 第 7 步：使用 `skill-authoring` 迭代 Skill

当某个经验经过多次验证，确实值得沉淀成流程时，再使用 `skill-authoring`。

#### 输入方式

```text
请使用 skill-authoring skill，根据刚才 session-retrospective 的结论，生成或改进 Skill。

要求：
1. 判断应该更新 common、已有 Skill，还是新增 Skill。
2. 只沉淀已验证、可复用、长期有效的内容。
3. 输出具体修改文件和 patch。
4. 不写入密钥、Token、隐私、临时日志、未验证猜测。
```

#### 输出验收标准

AI 应该输出：

```text
建议修改位置
修改原因
完整 patch 或完整文件内容
是否影响 Claude / Codex / Cursor 适配
是否需要更新 README 或 docs
```

#### 你需要人工做的事

```text
1. 审查 Skill 改动是否过度泛化。
2. 检查是否把项目特有规则写进公共 Skill。
3. 检查是否包含敏感信息。
4. 使用 code-review skill 审查 Skill 本身。
5. 提交到 ai-engineering-skills 仓库。
```

---

## 十、第二周以后推荐用法

### 安全审查

```text
请使用 security-review skill 审查本次改动，重点关注：
1. 密钥泄露
2. Token 暴露
3. 越权访问
4. 权限绕过
5. SQL 注入 / XSS / 命令注入
6. 日志隐私泄露
7. 客户端硬编码敏感信息
```

#### 输出验收标准

```text
安全风险清单
风险等级
受影响文件
修复建议
是否阻塞合并
```

#### 你需要人工做的事

```text
1. 高风险安全问题必须人工复核。
2. 不要让 AI 自动修改权限系统或鉴权逻辑。
3. 对客户端硬编码、日志脱敏、越权访问重点检查。
```

### 性能审查

```text
请使用 performance-review skill 审查本次改动。
```

#### 输出验收标准

```text
性能风险点
可能影响范围
验证方法
优化建议
是否阻塞发版
```

#### 你需要人工做的事

```text
1. 检查是否有真实数据或工具验证。
2. 对启动耗时、接口耗时、主线程阻塞、慢查询重点复核。
3. 不要只凭 AI 推测就做复杂优化。
```

### CI 修复

```text
请使用 build-ci-fix skill 分析这段 CI 失败日志，并给出最小修复方案。
```

#### 输出验收标准

```text
失败阶段
关键错误
根因假设
最小修复方案
需要运行的验证命令
```

#### 你需要人工做的事

```text
1. 不允许为了通过 CI 删除测试。
2. 不允许随意降低 Lint / Check 规则。
3. 确认修复是否影响业务逻辑。
```

---

## 十一、线上问题处理流程

### 第 1 步：监控分析

```text
请使用 monitoring-analysis skill 分析这个监控异常。

异常信息：
【粘贴告警 / 指标 / 链接 / 时间范围】

要求：
1. 明确异常开始时间
2. 按版本、平台、地区、渠道、机型拆分
3. 对比最近发版和配置变更
4. 区分已确认事实和根因假设
```

#### 输出验收标准

```text
异常指标
开始时间
影响范围
拆分维度
已确认事实
根因假设
下一步排查建议
```

#### 你需要人工做的事

```text
1. 确认 AI 使用的数据是否可靠。
2. 确认时间范围是否正确。
3. 不要只看单一指标就下结论。
4. 必要时补充日志、Crash、发版记录。
```

### 第 2 步：Bug 定位

```text
请使用 bug-triage skill 定位这个线上问题。

已知信息：
1. 用户反馈：
2. 影响版本：
3. 时间范围：
4. 相关日志：
5. 最近发版：
6. 相关 commit：
```

#### 输出验收标准

```text
问题现象
影响范围
已确认事实
根因假设
证据
建议止血方案
建议修复方案
回滚建议
还需补充的信息
```

#### 你需要人工做的事

```text
1. 检查 AI 是否有证据支撑根因。
2. 如果证据不足，不允许直接修复。
3. 判断是否需要先回滚或关闭开关。
4. 高风险修复必须人工审批。
```

### 第 3 步：事故应急

```text
请使用 incident-response skill，基于当前线上问题给出应急处理方案。
```

#### 输出验收标准

```text
事故等级
影响范围
当前状态
止血方案
回滚 / 降级建议
通知对象
下一步动作
需要记录的时间线
```

#### 你需要人工做的事

```text
1. 判断是否先止血再修复。
2. 判断是否需要通知负责人、测试、运维、产品。
3. 人工确认回滚、降级、限流、关闭开关等操作。
4. 记录所有关键时间点。
```

### 第 4 步：事故复盘

```text
请使用 postmortem skill，基于本次事故生成复盘报告。
```

#### 输出验收标准

```text
事故摘要
影响范围
时间线
根因分析
处理过程
做得好的地方
问题与不足
短期改进
长期防线
需要沉淀到 Skills 的内容
```

#### 你需要人工做的事

```text
1. 确认时间线准确。
2. 确认复盘不甩锅，聚焦系统改进。
3. 把长期防线转成明确 action item。
4. 将可复用经验交给 session-retrospective / skill-authoring 沉淀。
```

---

## 十二、使用原则

1. Skill 不是越多越好，而是高频、稳定、可复用的流程才沉淀。
2. `skills/common/` 放跨 Skill 通用规则，例如安全、证据、风险分级、输出格式。
3. 具体业务规则优先放业务项目的 `CLAUDE.md` / `AGENTS.md`，不要硬编码到公共 Skill。
4. 每次使用后都要问：本次会话有没有值得沉淀为 common 或 Skill 的内容？
5. 不要把临时日志、密钥、Token、用户隐私写入长期上下文。
6. 不要把未经验证的猜测沉淀为规则。
7. 不要让 AI 自动合并主干、自动正式发版、自动修改生产数据。

---

## 十三、推荐演进路线

### 第一周

目标：跑通本地 AI Coding 工作流。

```text
context-bootstrap
requirement-analysis
technical-design
test-case-generation
android-development / ios-development / backend-development
code-review
session-retrospective
```

### 第二周

目标：增强质量和稳定性。

```text
security-review
performance-review
build-ci-fix
api-design
data-model-design
```

### 第三周

目标：进入线上问题处理。

```text
monitoring-analysis
bug-triage
incident-response
postmortem
```

### 第四周以后

目标：接入团队协作和自动化。

```text
飞书 / Slack 群机器人
GitHub / GitLab PR
CI/CD 日志
Crash 平台
监控平台
只读日志查询
自动生成 MR
人工 Review 后合并
```

---

## 十四、关键边界

AI 可以做：

```text
分析需求
生成技术方案
写低风险代码
生成测试用例
审查 diff
分析日志
提出修复建议
生成 MR 描述
沉淀经验
```

AI 不应该直接做：

```text
合并主干
正式发版
修改生产数据库
删除生产数据
绕过权限
提交密钥
更改支付 / 登录 / 权限等高风险模块而不审批
```

---

## 十五、维护建议

每次迭代本仓库时，建议遵循：

```text
先由 session-retrospective 判断是否值得沉淀
再由 skill-authoring 生成或修改 Skill
然后由 code-review 审查 Skill 本身
最后提交到 ai-engineering-skills 仓库
```

推荐提交信息：

```text
improve android-development skill
add security-review skill
update common security rules
add incident-response workflow
```

---

## 十六、最小落地清单

第一次落地时，只要完成下面这些，就算跑通了：

```text
1. 业务项目已添加 .ai/ai-engineering-skills submodule。
2. 业务项目根目录已有 CLAUDE.md。
3. 业务项目根目录已有 AGENTS.md。
4. AI 已执行 context-bootstrap。
5. AI 已完成一次 requirement-analysis。
6. AI 已完成一次 technical-design。
7. AI 已完成一次 development。
8. AI 已完成一次 code-review。
9. AI 已完成一次 session-retrospective。
10. 至少有一条经验被沉淀到 CLAUDE.md、AGENTS.md、docs 或 Skills。
```
