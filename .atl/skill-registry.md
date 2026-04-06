# Skill Registry — portafolio-template

Generated: 2026-04-01
Stack: Python / Reflex 0.4.5

## User Skills

| Skill | Trigger | Source |
|-------|---------|--------|
| issue-creation | Creating GitHub issues, reporting bugs, requesting features | user-global |
| branch-pr | Creating PRs, opening PRs, preparing changes for review | user-global |
| skill-creator | Creating new AI skills, adding agent instructions | user-global |
| go-testing | Writing Go tests, Bubbletea TUI testing | user-global |
| judgment-day | "judgment day", "dual review", "doble review", "juzgar" | user-global |

## Project Convention Files

| File | Path | Scope |
|------|------|-------|
| AGENTS.md | AGENTS.md | project |
| AGENTS.md (global) | ~/.config/opencode/AGENTS.md | user-global |

## Compact Rules

### From AGENTS.md (project)

- Reflex Standard: Use exclusively Reflex components and style system (Python dicts). No native HTML/CSS.
- SDD Workflow mandatory: Spec -> Design -> Tasks -> Apply -> Verify. No code without a validated task.
- PEP 8 naming. Descriptive English names for UI functions/variables.
- Conventional Commits (e.g. `feat: add tech stack component`). Atomic commits per completed task.
- Gitflow model. `main` branch is protected (production). All changes via PR.
- SOLID and GRASP principles for design and implementation.
- Data source of truth: `assets/data/data.json`. All dynamic content from there.
- No hardcoded sensitive info. CV and images managed from `assets/` only.
- Manual QA required: human confirmation after local deploy before archive.

### From AGENTS.md (user-global)

- Conventional commits only. Never add "Co-Authored-By" or AI attribution.
- Never build after changes.
- When asking a question, STOP and wait for response.
- Verify claims before stating. If unsure, investigate first.
- Respond in same language as user. Warm, professional, direct tone.
