# Submodule Usage

添加：

```powershell
git submodule add https://github.com/<your-org-or-username>/ai-engineering-skills.git .ai/ai-engineering-skills
git submodule update --init --recursive
```

更新：

```powershell
git submodule update --remote .ai/ai-engineering-skills
git add .ai/ai-engineering-skills
git commit -m "update ai engineering skills"
```

克隆包含 submodule 的项目：

```powershell
git clone --recurse-submodules <repo>
```
