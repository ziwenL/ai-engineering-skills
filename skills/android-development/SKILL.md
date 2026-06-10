---
name: android-development
description: 用于 Android 功能开发、Bug 修复、页面状态、接口接入和测试验证。
---

# Android 开发 Skill

## 适用场景

- Android 新功能开发
- Android Bug 修复
- 页面状态和接口接入调整
- 在现有架构下做最小可行改动

## 输入

- 已确认的需求分析
- 已确认的技术方案
- 项目入口文件和 `skills/common/`
- Android 相似实现
- `architecture.md`
- `checklist.md`

## 工作流程

1. 阅读需求分析和技术方案。
2. 阅读项目入口文件和 `skills/common/`。
3. 阅读 `architecture.md`，确认不能绕过现有分层和状态管理方式。
4. 阅读 `checklist.md`，把检查项当作实现和收尾清单。
5. 查找 Android 项目中相似模块。
6. 先列出计划修改文件和原因。
7. 按最小可行改动实现。
8. 补充 loading / empty / error / success 状态，并检查权限、网络、超时和重试。
9. 运行相关编译或测试命令。
10. 输出修改摘要、验证结果、未验证项和风险。

## Windows 验证命令示例

```powershell
.\gradlew.bat assembleDebug
.\gradlew.bat test
.\gradlew.bat lint
```

## macOS / Linux 验证命令示例

```bash
./gradlew assembleDebug
./gradlew test
./gradlew lint
```

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
- 不能声称“已验证”而没有运行对应命令或明确说明无法运行原因。

## 不适用场景

- 纯 iOS、服务端或前端任务
- 仍处于需求不清或技术方案未确认的任务
- 需要先做人审批准的高风险系统级改造
