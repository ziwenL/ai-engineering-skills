# Android 架构参考

默认建议：

- UI 层不直接访问网络或数据库。
- ViewModel 负责状态管理。
- Repository 负责数据获取。
- Domain / UseCase 负责业务规则。
- 错误统一封装。
- 不要绕过已有架构。
