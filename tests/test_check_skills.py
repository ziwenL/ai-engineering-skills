import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest
import os
import importlib.util
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CHECK_SCRIPT = REPO_ROOT / "scripts" / "check_skills.py"
CHECK_SCRIPT_SPEC = importlib.util.spec_from_file_location("check_skills_module", CHECK_SCRIPT)
CHECK_SCRIPT_MODULE = importlib.util.module_from_spec(CHECK_SCRIPT_SPEC)
assert CHECK_SCRIPT_SPEC is not None and CHECK_SCRIPT_SPEC.loader is not None
CHECK_SCRIPT_SPEC.loader.exec_module(CHECK_SCRIPT_MODULE)


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(content).strip() + "\n", encoding="utf-8")


class CheckSkillsScriptTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = Path(tempfile.mkdtemp(prefix="skill-check-"))
        (self.temp_dir / "skills").mkdir()

    def tearDown(self) -> None:
        shutil.rmtree(self.temp_dir)

    def run_check(self) -> subprocess.CompletedProcess[str]:
        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "utf-8"
        return subprocess.run(
            [sys.executable, str(CHECK_SCRIPT), str(self.temp_dir)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
            env=env,
        )

    def test_passes_for_skill_with_required_sections_and_referenced_support_file(self) -> None:
        write_text(
            self.temp_dir / "skills" / "backend-development" / "SKILL.md",
            """
            ---
            name: backend-development
            description: 示例
            ---

            # 服务端开发 Skill

            ## 适用场景
            - 新接口开发

            ## 输入
            - 已确认需求

            ## 工作流程
            1. 先阅读 `api-checklist.md`
            2. 再实现最小改动

            ## 输出格式
            ```text
            【修改文件】
            【验证结果】
            【未验证项】
            ```

            ## 约束
            - 不做无关重构

            ## 不适用场景
            - 纯前端任务
            """,
        )
        write_text(
            self.temp_dir / "skills" / "backend-development" / "api-checklist.md",
            """
            # API Checklist
            - [ ] 入参
            """,
        )

        result = self.run_check()

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("[OK] backend-development", result.stdout)

    def test_fails_when_required_section_is_missing(self) -> None:
        write_text(
            self.temp_dir / "skills" / "frontend-development" / "SKILL.md",
            """
            ---
            name: frontend-development
            description: 示例
            ---

            # 前端开发 Skill

            ## 适用场景
            - 页面开发

            ## 工作流程
            1. 实现页面

            ## 输出格式
            ```text
            【修改摘要】
            ```

            ## 约束
            - 不做无关重构

            ## 不适用场景
            - 纯后端任务
            """,
        )

        result = self.run_check()

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("缺少必需章节", result.stdout)
        self.assertIn("## 输入", result.stdout)

    def test_fails_when_support_file_is_not_referenced(self) -> None:
        write_text(
            self.temp_dir / "skills" / "security-review" / "SKILL.md",
            """
            ---
            name: security-review
            description: 示例
            ---

            # 安全审查 Skill

            ## 适用场景
            - 安全审查

            ## 输入
            - 代码改动

            ## 工作流程
            1. 先看代码

            ## 输出格式
            ```text
            【风险】
            ```

            ## 约束
            - 证据不足时不要下结论

            ## 不适用场景
            - 非代码任务
            """,
        )
        write_text(
            self.temp_dir / "skills" / "security-review" / "checklist.md",
            """
            # Security Checklist
            - [ ] 敏感信息
            """,
        )

        result = self.run_check()

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("未引用的辅助文件", result.stdout)
        self.assertIn("checklist.md", result.stdout)

    def test_fails_when_development_skill_lacks_verification_language(self) -> None:
        write_text(
            self.temp_dir / "skills" / "frontend-development" / "SKILL.md",
            """
            ---
            name: frontend-development
            description: 示例
            ---

            # 前端开发 Skill

            ## 适用场景
            - 页面开发

            ## 输入
            - 已确认需求

            ## 工作流程
            1. 修改页面

            ## 输出格式
            ```text
            【修改摘要】
            【风险点】
            ```

            ## 约束
            - 不做无关重构

            ## 不适用场景
            - 纯后端任务
            """,
        )

        result = self.run_check()

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("开发类 Skill 缺少关键信息", result.stdout)
        self.assertIn("验证", result.stdout)
        self.assertIn("未验证项", result.stdout)

    def test_fails_when_review_skill_lacks_evidence_and_blocker_language(self) -> None:
        write_text(
            self.temp_dir / "skills" / "code-review" / "SKILL.md",
            """
            ---
            name: code-review
            description: 示例
            ---

            # 代码审查 Skill

            ## 适用场景
            - 审查 diff

            ## 输入
            - diff

            ## 工作流程
            1. 查看改动

            ## 输出格式
            ```text
            【结论】
            【问题】
            ```

            ## 约束
            - 聚焦风险

            ## 不适用场景
            - 无 diff 的场景
            """,
        )

        result = self.run_check()

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("审查类 Skill 缺少关键信息", result.stdout)
        self.assertIn("证据", result.stdout)
        self.assertIn("风险等级", result.stdout)
        self.assertIn("是否阻塞", result.stdout)

    def test_passes_for_android_to_ios_bootstrap_with_referenced_checklist(self) -> None:
        write_text(
            self.temp_dir / "skills" / "android-to-ios-bootstrap" / "SKILL.md",
            """
            ---
            name: android-to-ios-bootstrap
            description: 示例
            ---

            # Android 到 iOS 启动 Skill

            ## 适用场景
            - Android 已有实现，iOS 状态不明确

            ## 输入
            - Android 代码
            - `bootstrap-checklist.md`

            ## 工作流程
            1. 读取 `bootstrap-checklist.md`
            2. 判断 iOS 状态

            ## 输出格式
            ```text
            【建议下一步 Skill】
            【验证方式】
            【未验证项】
            ```

            ## 约束
            - 不要直接进入完整实现

            ## 不适用场景
            - Android 尚未稳定
            """,
        )
        write_text(
            self.temp_dir / "skills" / "android-to-ios-bootstrap" / "bootstrap-checklist.md",
            """
            # Bootstrap Checklist
            - [ ] iOS 项目是否存在
            """,
        )

        result = self.run_check()

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("[OK] android-to-ios-bootstrap", result.stdout)

    def test_fails_when_android_to_ios_bootstrap_checklist_is_not_referenced(self) -> None:
        write_text(
            self.temp_dir / "skills" / "android-to-ios-bootstrap" / "SKILL.md",
            """
            ---
            name: android-to-ios-bootstrap
            description: 示例
            ---

            # Android 到 iOS 启动 Skill

            ## 适用场景
            - Android 已有实现，iOS 状态不明确

            ## 输入
            - Android 代码

            ## 工作流程
            1. 判断 iOS 状态

            ## 输出格式
            ```text
            【建议下一步 Skill】
            【验证方式】
            【未验证项】
            ```

            ## 约束
            - 不要直接进入完整实现

            ## 不适用场景
            - Android 尚未稳定
            """,
        )
        write_text(
            self.temp_dir / "skills" / "android-to-ios-bootstrap" / "bootstrap-checklist.md",
            """
            # Bootstrap Checklist
            - [ ] iOS 项目是否存在
            """,
        )

        result = self.run_check()

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("未引用的辅助文件", result.stdout)
        self.assertIn("bootstrap-checklist.md", result.stdout)

    def test_fails_when_android_to_ios_bootstrap_lacks_unverified_item_language(self) -> None:
        write_text(
            self.temp_dir / "skills" / "android-to-ios-bootstrap" / "SKILL.md",
            """
            ---
            name: android-to-ios-bootstrap
            description: 示例
            ---

            # Android 到 iOS 启动 Skill

            ## 适用场景
            - Android 已有实现，iOS 状态不明确

            ## 输入
            - Android 代码

            ## 工作流程
            1. 判断 iOS 状态

            ## 输出格式
            ```text
            【建议下一步 Skill】
            【风险点】
            ```

            ## 约束
            - 不要直接进入完整实现

            ## 不适用场景
            - Android 尚未稳定
            """,
        )

        result = self.run_check()

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("开发类 Skill 缺少关键信息", result.stdout)
        self.assertIn("未验证项", result.stdout)


    def test_passes_for_greenfield_bootstrap_with_referenced_checklist(self) -> None:
        write_text(
            self.temp_dir / "skills" / "greenfield-bootstrap" / "SKILL.md",
            """
            ---
            name: greenfield-bootstrap
            description: 示例
            ---

            # Greenfield Bootstrap Skill

            ## 适用场景
            - 从 0 创建新项目
            ## 输入
            - 已确认目标
            - `bootstrap-checklist.md`

            ## 工作流程
            1. 读取 `bootstrap-checklist.md`
            2. 判断启动顺序

            ## 输出格式
            ```text
            【推荐启动顺序】
            【验证方式】
            【未验证项】
            ```

            ## 约束
            - 不直接展开完整实现

            ## 不适用场景
            - 已有稳定项目继续开发
            """,
        )
        write_text(
            self.temp_dir / "skills" / "greenfield-bootstrap" / "bootstrap-checklist.md",
            """
            # Bootstrap Checklist
            - [ ] 是否需要多端联动启动
            """,
        )

        result = self.run_check()

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("[OK] greenfield-bootstrap", result.stdout)

    def test_passes_for_android_app_scaffold_with_referenced_support_files(self) -> None:
        write_text(
            self.temp_dir / "skills" / "android-app-scaffold" / "SKILL.md",
            """
            ---
            name: android-app-scaffold
            description: 示例
            ---

            # Android App Scaffold Skill

            ## 适用场景
            - 创建 Android 新项目骨架
            ## 输入
            - 已确认目标
            - `scaffold-checklist.md`
            - `default-stack.md`

            ## 工作流程
            1. 读取 `scaffold-checklist.md`
            2. 读取 `default-stack.md`
            3. 生成最小骨架

            ## 输出格式
            ```text
            【推荐默认方案】
            【验证方式】
            【未验证项】
            ```

            ## 约束
            - 只创建最小可运行骨架

            ## 不适用场景
            - 已有稳定 Android 项目继续开发
            """,
        )
        write_text(
            self.temp_dir / "skills" / "android-app-scaffold" / "scaffold-checklist.md",
            """
            # Scaffold Checklist
            - [ ] 是否确实需要多模块
            """,
        )
        write_text(
            self.temp_dir / "skills" / "android-app-scaffold" / "default-stack.md",
            """
            # Default Stack
            - 默认：Jetpack Compose
            - Compose Coding Convention
            - Every reusable UI component must provide @Preview
            - Business Screen with ViewModel injection does not require @Preview
            - Preview data should use fake/mock data
            - Preview function should be private
            - Preview should not contain network/database dependency
            """,
        )

        result = self.run_check()

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("[OK] android-app-scaffold", result.stdout)

    def test_fails_when_android_development_lacks_compose_preview_conventions(self) -> None:
        write_text(
            self.temp_dir / "skills" / "android-development" / "SKILL.md",
            """
            ---
            name: android-development
            description: 示例
            ---

            # Android 开发 Skill

            ## 适用场景
            - Android 功能开发

            ## 输入
            - 已确认需求
            - `checklist.md`

            ## 工作流程
            1. 阅读 `checklist.md`
            2. 实现最小改动
            3. 运行验证命令

            ## 输出格式
            ```text
            【验证结果】
            【未验证项】
            ```

            ## 约束
            - 不做无关重构

            ## 不适用场景
            - 纯 iOS 任务
            """,
        )
        write_text(
            self.temp_dir / "skills" / "android-development" / "checklist.md",
            """
            # Android Checklist
            - [ ] 验证
            """,
        )

        result = self.run_check()

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Compose Preview", result.stdout)
        self.assertIn("@Preview", result.stdout)

    def test_passes_for_ios_app_scaffold_with_referenced_support_files(self) -> None:
        sections = "\n\n".join(
            (
                f"{CHECK_SCRIPT_MODULE.REQUIRED_SECTIONS[0]}\n- 创建 iOS 新项目骨架",
                f"{CHECK_SCRIPT_MODULE.REQUIRED_SECTIONS[1]}\n- 已确认目标\n- `scaffold-checklist.md`\n- `default-stack.md`",
                f"{CHECK_SCRIPT_MODULE.REQUIRED_SECTIONS[2]}\n1. 读取 `scaffold-checklist.md`\n2. 读取 `default-stack.md`\n3. 生成最小骨架",
                f"{CHECK_SCRIPT_MODULE.REQUIRED_SECTIONS[3]}\n```text\n【推荐默认方案】\n【{CHECK_SCRIPT_MODULE.DEVELOPMENT_REQUIRED_FRAGMENTS[0]}方式】\n【{CHECK_SCRIPT_MODULE.DEVELOPMENT_REQUIRED_FRAGMENTS[1]}】\n```",
                f"{CHECK_SCRIPT_MODULE.REQUIRED_SECTIONS[4]}\n- 只创建最小可运行骨架",
                f"{CHECK_SCRIPT_MODULE.REQUIRED_SECTIONS[5]}\n- 已有稳定 iOS 项目继续开发",
            )
        )
        skill_text = "\n".join(
            (
                "---",
                "name: ios-app-scaffold",
                "description: 示例",
                "---",
                "",
                "# iOS App Scaffold Skill",
                "",
                sections,
            )
        )
        write_text(
            self.temp_dir / "skills" / "ios-app-scaffold" / "SKILL.md",
            skill_text,
        )
        write_text(
            self.temp_dir / "skills" / "ios-app-scaffold" / "scaffold-checklist.md",
            """
            # Scaffold Checklist
            - [ ] 鏄惁鍙渶瑕佸崟宸ョ▼璧锋
            """,
        )
        write_text(
            self.temp_dir / "skills" / "ios-app-scaffold" / "default-stack.md",
            """
            # Default Stack
            - 榛樿锛歋wiftUI
            """,
        )

        result = self.run_check()

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("[OK] ios-app-scaffold", result.stdout)

    def test_fails_when_greenfield_bootstrap_checklist_is_not_referenced(self) -> None:
        write_text(
            self.temp_dir / "skills" / "greenfield-bootstrap" / "SKILL.md",
            """
            ---
            name: greenfield-bootstrap
            description: 示例
            ---

            # Greenfield Bootstrap Skill

            ## 适用场景
            - 从 0 创建新项目
            ## 输入
            - 已确认目标

            ## 工作流程
            1. 判断启动顺序

            ## 输出格式
            ```text
            【推荐启动顺序】
            【验证方式】
            【未验证项】
            ```

            ## 约束
            - 不直接展开完整实现

            ## 不适用场景
            - 已有稳定项目继续开发
            """,
        )
        write_text(
            self.temp_dir / "skills" / "greenfield-bootstrap" / "bootstrap-checklist.md",
            """
            # Bootstrap Checklist
            - [ ] 是否需要多端联动启动
            """,
        )

        result = self.run_check()

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("未引用的辅助文件", result.stdout)
        self.assertIn("bootstrap-checklist.md", result.stdout)

    def test_fails_when_backend_service_scaffold_lacks_unverified_item_language(self) -> None:
        write_text(
            self.temp_dir / "skills" / "backend-service-scaffold" / "SKILL.md",
            """
            ---
            name: backend-service-scaffold
            description: 示例
            ---

            # Backend Service Scaffold Skill

            ## 适用场景
            - 创建服务端骨架
            ## 输入
            - 已确认目标
            - `scaffold-checklist.md`
            - `default-stack.md`

            ## 工作流程
            1. 读取 `scaffold-checklist.md`
            2. 读取 `default-stack.md`

            ## 输出格式
            ```text
            【推荐默认方案】
            【初始化步骤】
            ```

            ## 约束
            - 只创建最小可运行骨架

            ## 不适用场景
            - 已有稳定服务继续开发
            """,
        )
        write_text(
            self.temp_dir / "skills" / "backend-service-scaffold" / "scaffold-checklist.md",
            """
            # Scaffold Checklist
            - [ ] 是否需要数据库
            """,
        )
        write_text(
            self.temp_dir / "skills" / "backend-service-scaffold" / "default-stack.md",
            """
            # Default Stack
            - 默认：轻量 REST 服务
            """,
        )

        result = self.run_check()

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("开发类 Skill 缺少关键信息", result.stdout)
        self.assertIn("未验证项", result.stdout)


if __name__ == "__main__":
    unittest.main()
