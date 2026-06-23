# Android 开发检查清单

- [ ] 是否找到相似实现
- [ ] 是否说明修改文件
- [ ] 是否处理 loading / empty / error / success
- [ ] 是否处理权限、网络异常、超时和重试
- [ ] 可复用 Compose UI 组件是否提供 `@Preview`
- [ ] 业务 Screen 如果因 `ViewModel` injection 不提供 `@Preview`，是否已明确说明
- [ ] Preview data 是否使用 `fake/mock` data
- [ ] Preview function 是否为 `private`
- [ ] Preview 是否不包含 `network/database` dependency
- [ ] 是否运行编译、lint 或测试命令
- [ ] 是否没有修改无关文件
