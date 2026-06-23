---
name: android-development
description: 用于 Android 功能开发、Bug 修复、页面状态处理、接口接入和测试验证。
---

# Android 开发 Skill

## 适用场景

- Android 新功能开发
- Android Bug 修复
- 页面状态、接口接入或交互边界调整
- 在现有架构下做最小可行改动

## 输入

- 已确认的需求分析
- 已确认的技术方案
- 项目入口文档和 `skills/common/`
- Android 侧相似实现
- `architecture.md`
- `checklist.md`
- `usage-examples.md`

## 工作流程

1. 阅读需求分析和技术方案。
2. 阅读项目入口文档和 `skills/common/`，确认当前项目约束。
3. 阅读 `architecture.md`，确认不能绕过现有分层和状态管理方式。
4. 阅读 `checklist.md`，把检查项当作实现和收尾清单。
5. 查找 Android 项目中的相似页面、状态处理、接口接入或 Compose 组件实现。
6. 先列出计划修改的文件和原因。
7. 如果本次修改涉及 Jetpack Compose，可复用 UI 组件必须遵守 Compose Coding Convention：
   - Every reusable UI component must provide `@Preview`
   - Business Screen with `ViewModel` injection does not require `@Preview`
   - Preview data should use `fake/mock` data
   - Preview function should be `private`
   - Preview should not contain `network/database` dependency
8. 按最小可行改动实现需求。
9. 补齐 loading / empty / error / success 状态，并检查权限、网络异常、超时和重试边界。
10. 运行相关编译、测试或 lint 命令完成验证。
11. 输出修改摘要、验证结果、未验证项和风险点。

## 输出格式

```text
【修改文件列表】
【每个文件的修改原因】
【核心实现逻辑】
【状态与异常处理】
【验证命令与结果】
【未验证项】
【风险点】
【人工验证建议】
```

## 约束

- 不做无关重构。
- 不引入新依赖，除非先得到确认。
- 不绕过 `architecture.md` 中已有架构约束。
- 必须使用 `checklist.md` 逐项自检。
- 如果新增或修改可复用 Compose UI 组件，必须补 `@Preview`；若不补，必须明确说明它是带 `ViewModel` injection 的业务 Screen。
- Preview 数据必须使用 `fake/mock` data，且 Preview function 必须是 `private`。
- Preview 不能包含 `network/database` dependency。
- 没有运行验证命令时，不能声称“已验证”；必须明确说明原因。

## 不适用场景

- 纯 iOS、纯服务端或纯前端任务
- 仍处于需求不清或技术方案未确认的任务
- 需要先做人工批准的高风险系统级改造

## 使用示例

最小调用示例：

```text
请使用 android-development skill 实现该需求。
请先阅读：
1. 已确认的需求分析
2. 已确认的技术方案
3. 项目入口文档
4. skills/common/
5. skills/android-development/architecture.md
6. skills/android-development/checklist.md
7. Android 侧相似实现

要求：
- 先列出计划修改的文件和原因。
- 遵守当前项目架构。
- 不要修改与需求无关的代码。
- 如果涉及可复用 Compose 组件，按 Compose Coding Convention 处理 @Preview。
- 实现后运行相关编译或测试命令。

最后输出：
1. 修改摘要
2. 验证结果
3. 未验证项
4. 风险点
```

更多示例见 `usage-examples.md`。
