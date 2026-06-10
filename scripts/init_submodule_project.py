#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Initialize a business project after ai-engineering-skills has been added as a Git submodule.

Usage:
    python scripts/init_submodule_project.py "C:/Users/<your-username>/Projects/your-business-project"

Expected submodule path:
    .ai/ai-engineering-skills
"""

from pathlib import Path
import shutil
import sys

def copy_if_missing(src: Path, dst: Path):
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        print(f"[SKIP] {dst.name} already exists")
        return
    shutil.copy2(src, dst)
    print(f"[OK] Created {dst}")

def main():
    if len(sys.argv) < 2:
        print('Usage: python scripts/init_submodule_project.py "C:/Users/<your-username>/Projects/your-business-project"')
        sys.exit(1)

    project = Path(sys.argv[1]).expanduser().resolve()
    if not project.exists():
        print(f"Project does not exist: {project}")
        sys.exit(1)

    skills_repo = project / ".ai" / "ai-engineering-skills"
    if not skills_repo.exists():
        print(f"Missing submodule: {skills_repo}")
        print("Please run:")
        print("git submodule add https://github.com/<your-org-or-username>/ai-engineering-skills.git .ai/ai-engineering-skills")
        sys.exit(2)

    copy_if_missing(skills_repo / "adapters" / "claude" / "CLAUDE.md.template", project / "CLAUDE.md")
    copy_if_missing(skills_repo / "adapters" / "codex" / "AGENTS.md.template", project / "AGENTS.md")

    for d in [
        project / "docs" / "decisions",
        project / "docs" / "incident-history",
        project / "docs" / "ai-sessions",
    ]:
        d.mkdir(parents=True, exist_ok=True)
        print(f"[OK] Ensured {d}")

    print("Done.")

if __name__ == "__main__":
    main()
