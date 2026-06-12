# 使用示例

## 说明

这个 Skill 适合在 Android 项目中做功能开发、Bug 修复或结构内演进。示例强调遵守现有架构、先找相似实现、再做最小改动并验证。

## 最小调用示例

```text
请使用 android-development skill 实现该需求。

请先阅读：
1. 已确认的需求分析
2. 已确认的技术方案
3. 项目入口文档
4. skills/common/
5. skills/android-development/architecture.md
6. skills/android-development/checklist.md
7. Android 端相似实现

要求：
- 先列出计划修改的文件和原因。
- 遵守当前项目架构。
- 不要修改与需求无关的代码。
- 实现后运行相关编译或测试命令。

最后输出：
1. 修改摘要
2. 验证结果
3. 未验证项
4. 风险点
```

## 推荐调用示例

```text
请使用 android-development skill 在当前 Android 项目中实现这个需求。

请按以下顺序进行：
1. 阅读需求分析和技术方案
2. 阅读项目入口文档和 skills/common/
3. 阅读 skills/android-development/architecture.md
4. 阅读 skills/android-development/checklist.md
5. 查找 Android 项目中的相似页面、状态处理或接口接入实现

实现要求：
1. 先列出计划修改的文件清单和每个文件的修改原因
2. 严格遵守当前架构和状态管理方式
3. 不要引入新依赖，除非先明确说明必要性
4. 补齐 loading / empty / error / success 等必要状态
5. 检查网络异常、超时、重试、权限等边界
6. 不做与当前需求无关的重构

完成后请输出：
1. 修改文件列表
2. 核心实现逻辑
3. 状态与异常处理
4. 验证命令与结果
5. 未验证项
6. 风险点
7. 人工验证建议
```

## 高约束调用示例

```text
请使用 android-development skill 实现当前需求，并保持最小改动原则。

必须先阅读：
1. 已确认的需求分析
2. 已确认的技术方案
3. 项目入口文档
4. skills/common/
5. skills/android-development/architecture.md
6. skills/android-development/checklist.md
7. Android 项目中的相似实现

执行要求：
- 先输出计划修改文件清单，不要直接开改。
- 不要绕过既有架构边界。
- 不要顺手做无关重构。
- 如果无法运行验证命令，要明确说明原因。

请严格按以下结构输出：
【修改文件列表】
【每个文件的修改原因】
【核心实现逻辑】
【状态与异常处理】
【验证命令与结果】
【未验证项】
【风险点】
【人工验证建议】
```

## 适用提醒

- 适合已有 Android 项目内的功能实现与修复。
- 如果 Android 项目还没创建，应优先使用 `android-app-scaffold`。
- 如果还没有技术方案，建议先走 `technical-design`。
