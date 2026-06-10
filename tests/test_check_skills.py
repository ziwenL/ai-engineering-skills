import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest
import os
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CHECK_SCRIPT = REPO_ROOT / "scripts" / "check_skills.py"


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


if __name__ == "__main__":
    unittest.main()
