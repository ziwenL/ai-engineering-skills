#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import sys

REQUIRED = [
    ".ai/ai-engineering-skills/skills/common",
    ".ai/ai-engineering-skills/skills/context-bootstrap/SKILL.md",
    ".ai/ai-engineering-skills/skills/requirement-analysis/SKILL.md",
    ".ai/ai-engineering-skills/skills/technical-design/SKILL.md",
    ".ai/ai-engineering-skills/skills/session-retrospective/SKILL.md",
    "CLAUDE.md",
    "AGENTS.md",
    "docs/decisions",
    "docs/incident-history",
    "docs/ai-sessions",
]

def main():
    if len(sys.argv) < 2:
        print('Usage: python scripts/check_installation.py "C:/Users/<your-username>/Projects/your-business-project"')
        sys.exit(1)
    project = Path(sys.argv[1]).expanduser().resolve()
    ok = True
    for item in REQUIRED:
        p = project / item
        if p.exists():
            print(f"[OK] {item}")
        else:
            print(f"[MISSING] {item}")
            ok = False
    if not ok:
        sys.exit(2)
    print("Installation looks good.")

if __name__ == "__main__":
    main()
