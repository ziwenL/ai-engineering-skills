#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

from pathlib import Path
import re
import sys


REQUIRED_FRONTMATTER_KEYS = ("name", "description")
REQUIRED_SECTIONS = (
    "## 适用场景",
    "## 输入",
    "## 工作流程",
    "## 输出格式",
    "## 约束",
    "## 不适用场景",
)
DEVELOPMENT_SKILLS = {
    "android-development",
    "ios-development",
    "android-to-ios-bootstrap",
    "android-to-ios-porting",
    "api-design",
    "data-model-design",
    "technical-design",
    "test-case-generation",
    "build-ci-fix",
    "backend-development",
    "frontend-development",
}
REVIEW_SKILLS = {
    "code-review",
    "security-review",
    "performance-review",
}
DEVELOPMENT_REQUIRED_FRAGMENTS = ("验证", "未验证项")
REVIEW_REQUIRED_FRAGMENTS = ("证据", "风险等级", "是否阻塞")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\s*\n(.*?)\n---\s*(?:\n|$)", text, re.DOTALL)
    if not match:
        return {}

    result: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip()
    return result


def find_missing_sections(text: str) -> list[str]:
    return [section for section in REQUIRED_SECTIONS if section not in text]


def find_unreferenced_support_files(skill_dir: Path, text: str) -> list[str]:
    support_files = [
        path.name
        for path in sorted(skill_dir.iterdir())
        if path.is_file() and path.name != "SKILL.md"
    ]
    return [name for name in support_files if name not in text]


def find_missing_fragments(text: str, fragments: tuple[str, ...]) -> list[str]:
    return [fragment for fragment in fragments if fragment not in text]


def validate_skill(skill_dir: Path) -> list[str]:
    issues: list[str] = []
    skill_file = skill_dir / "SKILL.md"

    if not skill_file.exists():
        return [f"缺少文件: {skill_dir.name}/SKILL.md"]

    text = read_text(skill_file)
    frontmatter = parse_frontmatter(text)
    missing_keys = [key for key in REQUIRED_FRONTMATTER_KEYS if not frontmatter.get(key)]
    if missing_keys:
        issues.append(f"缺少 frontmatter 字段: {', '.join(missing_keys)}")

    missing_sections = find_missing_sections(text)
    if missing_sections:
        issues.append(f"缺少必需章节: {', '.join(missing_sections)}")

    unreferenced_files = find_unreferenced_support_files(skill_dir, text)
    if unreferenced_files:
        issues.append(f"未引用的辅助文件: {', '.join(unreferenced_files)}")

    if skill_dir.name in DEVELOPMENT_SKILLS:
        missing = find_missing_fragments(text, DEVELOPMENT_REQUIRED_FRAGMENTS)
        if missing:
            issues.append(f"开发类 Skill 缺少关键信息: {', '.join(missing)}")

    if skill_dir.name in REVIEW_SKILLS:
        missing = find_missing_fragments(text, REVIEW_REQUIRED_FRAGMENTS)
        if missing:
            issues.append(f"审查类 Skill 缺少关键信息: {', '.join(missing)}")

    return issues


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
    skills = root / "skills"
    if not skills.exists():
        print("Missing skills directory")
        return 1

    ok = True
    for skill_dir in sorted(skills.iterdir()):
        if not skill_dir.is_dir() or skill_dir.name == "common":
            continue

        issues = validate_skill(skill_dir)
        if issues:
            ok = False
            print(f"[FAIL] {skill_dir.name}")
            for issue in issues:
                print(f"  - {issue}")
        else:
            print(f"[OK] {skill_dir.name}")

    return 0 if ok else 2


if __name__ == "__main__":
    sys.exit(main())
