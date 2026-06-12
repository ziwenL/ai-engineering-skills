# 使用示例

## 说明

这个 Skill 适合在 Android 已有稳定实现的前提下，先判断 iOS 当前应该走哪条路：先建工程、先补结构，还是可以直接进入复刻。

## 最小调用示例

```text
请使用 android-to-ios-bootstrap skill，先判断当前任务应该如何进入 iOS 复刻流程。

已知信息：
1. Android 端已有实现
2. 当前产品需求与交互要求
3. iOS 当前状态：未创建 / 已创建但结构不稳 / 已创建且可复用

请输出：
1. iOS 当前状态判断
2. Android 现有行为概览
3. 是否需要先创建或补齐 iOS 工程
4. 推荐的下一步 Skill
5. 验证方式
6. 未验证项

要求：
- 不要直接写完整 iOS 功能代码。
- 行为一致优先于结构一致。
```

## 推荐调用示例

```text
请使用 android-to-ios-bootstrap skill，判断当前这个 Android 到 iOS 的复刻任务应该先进入哪条路径。

请先阅读：
1. Android 已实现代码
2. 已确认的产品需求与交互要求
3. 已知平台差异和限制
4. 当前 iOS 项目状态
5. skills/android-to-ios-bootstrap/bootstrap-checklist.md

请输出：
1. iOS 当前状态判断
2. Android 现有行为概览
3. 平台无关逻辑
4. 是否需要先创建或补齐 iOS 工程
5. 推荐的 iOS 工程结构
6. 首批应创建或修改的文件 / 模块
7. 必须保持一致的行为
8. 允许保留的平台差异
9. 建议下一步 Skill
10. 验证方式
11. 未验证项
12. 风险点

要求：
- 不要直接承担完整 iOS 功能实现。
- 不要机械翻译 Android 代码。
- 对无法确认的 iOS 工程状态明确写进未验证项。
```

## 高约束调用示例

```text
请使用 android-to-ios-bootstrap skill，严格判断当前任务应如何进入 iOS 复刻流程。

必须先阅读：
1. Android 已实现代码
2. 产品需求与交互要求
3. 已知平台差异
4. 当前 iOS 项目状态
5. skills/android-to-ios-bootstrap/bootstrap-checklist.md

请严格按以下结构输出：
【iOS 当前状态判断】
【Android 现有行为概览】
【平台无关逻辑】
【是否需要先创建或补齐 iOS 工程】
【推荐的 iOS 工程结构】
【首批应创建或修改的文件 / 模块】
【必须保持一致的行为】
【允许保留的平台差异】
【建议下一步 Skill】
【验证方式】
【未验证项】
【风险点】

要求：
- 不要直接进入完整 iOS 编码。
- 行为一致优先于结构一致。
- 无法确认的信息必须进入【未验证项】。
```

## 适用提醒

- 适合“Android 已有实现，但 iOS 该怎么起步还不确定”的场景。
- 如果 iOS 已具备稳定承接结构，下一步通常接 `android-to-ios-porting`。
- 如果项目本身还是从 0 起盘，应优先看 `greenfield-bootstrap`。
