# Android App Scaffold 检查清单

- [ ] 当前是否真的需要多模块，而不是先以单 `app` 模块起步
- [ ] 第一阶段是否只需要最小可运行壳子，而不是完整业务首页
- [ ] 是否需要预留网络层、登录态、本地存储、埋点或路由占位
- [ ] 是否已有团队偏好的包结构、命名规则、状态管理方式和构建约束
- [ ] 是否需要兼容后续与 Backend、iOS 的接口字段、错误码和环境配置对齐
- [ ] 如果默认采用 Jetpack Compose，是否已经写入 Compose Coding Convention
- [ ] 是否已经区分可复用组件的 `@Preview` 要求与带 `ViewModel` injection 的业务 Screen 例外
- [ ] Preview data 是否要求使用 `fake/mock` data
- [ ] Preview function 是否要求为 `private`
- [ ] Preview 是否明确不能依赖 `network/database`
- [ ] 哪些约束仍不明确，必须写入未验证项
