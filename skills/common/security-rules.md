# 安全规则

## 禁止沉淀到长期上下文

以下信息禁止写入 `skills/`、`CLAUDE.md`、`AGENTS.md`、`docs/`：

- 密钥
- Token
- 证书
- 用户隐私
- 生产数据库敏感信息
- 临时日志
- 未脱敏请求/响应
- 未验证猜测

## 生产环境规则

1. 生产数据库默认只读。
2. 生产日志必须脱敏后分析。
3. 不允许 AI 自动执行生产写操作。
4. 不允许 AI 自动发版。
5. 不允许 AI 自动合并主干。
6. 涉及支付、登录、权限、数据删除必须人工审批。

## Windows 高危命令

以下命令需要拦截或人工确认：

```powershell
Remove-Item -Recurse -Force
rmdir /s /q
del /s /q
format
diskpart
```

## Linux / macOS 高危命令

```bash
rm -rf /
rm -rf *
sudo rm -rf
chmod -R 777
```
