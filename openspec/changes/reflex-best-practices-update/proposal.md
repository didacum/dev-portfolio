# Proposal: Update Reflex Framework Implementation to Best Practices (v0.8+)

## Intent

Align the portfolio codebase with Reflex 0.8+ best practices, improving maintainability, responsiveness, and consistency. This includes fixing a persistent typo (`likedin` → `linkedin`), replacing deprecated Reflex patterns (`rx.cond` for static data, `rx.text.strong`), implementing responsive spacing/padding across all views, and centralizing component styles.

## Scope

### In Scope
- Fix `likedin` → `linkedin` in `data.json`, `data.py`, and `media.py`.
- Replace `rx.cond` with Python `if` statements for static data in `info_detail.py`.
- Replace `rx.text.strong` with `rx.strong` in `info_detail.py` and `card_detail.py`.
- Audit and adjust spacing/padding using the existing `Size` and `EmSize` enums across all views (`views/`) and the main layout (`portafolio.py`).
- Centralize repeated component styles into `styles.py` (e.g., common card styles, button variants).
- Ensure responsive behavior on mobile/desktop breakpoints where missing.

### Out of Scope
- Adding new features or changing existing functionality.
- Introducing automated tests (remains manual QA).
- Modifying the data schema beyond the typo fix.
- Updating Reflex version (already 0.8.28.post1).

## Capabilities

> This section is the CONTRACT between proposal and specs phases.

### New Capabilities
None (pure refactor and style improvements; no new user‑facing behavior).

### Modified Capabilities
None (existing spec‑level requirements unchanged).

## Approach

1. **Typo Fix**: Update the key in `data.json`, rename the field in `Media` dataclass, and update the reference in `media.py`.
2. **Deprecated Patterns**:
   - Replace `rx.text.strong` with `rx.strong` (direct component substitution).
   - Convert `rx.cond` blocks that guard static data (e.g., `info.technologies`, `info.url != ""`) to Python `if` statements, conditionally including the child components.
3. **Responsive Spacing**:
   - Audit each view component (`about`, `extra`, `footer`, `header`, `info`, `tech_stack`) for hard‑coded spacing values.
   - Replace with `Size`/`EmSize` constants and add breakpoint‑aware padding where needed (e.g., `padding_x=[Size.SMALL.value, Size.MEDIUM.value]`).
   - Review the main layout’s `padding_x`/`padding_y` for mobile‑first responsiveness.
4. **Style Centralization**:
   - Identify repeated style dictionaries (e.g., card shadows, button variants) and move them to `styles.py` as named constants.
   - Update components to reference these constants.

## Affected Areas

| Area | Impact | Description |
|------|--------|-------------|
| `assets/data/data.json` | Modified | Rename `likedin` key to `linkedin`. |
| `portafolio/data.py` | Modified | Change `Media.likedin` field to `linkedin`. |
| `portafolio/components/media.py` | Modified | Use `data.linkedin` instead of `data.likedin`. |
| `portafolio/components/info_detail.py` | Modified | Replace `rx.text.strong` with `rx.strong`; convert `rx.cond` to Python `if`. |
| `portafolio/components/card_detail.py` | Modified | Replace `rx.text.strong` with `rx.strong`. |
| `portafolio/styles/styles.py` | Modified | Add centralized style constants (e.g., `CARD_STYLE`, `BUTTON_VARIANT`). |
| `portafolio/views/` (all) | Modified | Adjust spacing/padding with responsive breakpoints. |
| `portafolio/portafolio.py` | Modified | Fine‑tune main layout padding for mobile/desktop. |

## Risks

| Risk | Likelihood | Mitigation |
|------|------------|------------|
| Breaking existing layout due to spacing changes | Low | Use the same numeric values as before, only converting to constants; verify visually after each change. |
| Over‑centralization making styles harder to maintain | Low | Keep constants close to where they are used (component‑level); only promote truly repeated patterns. |
| Missing a `rx.cond` that should stay reactive | Low | Only convert conditions that guard static data (empty strings, empty lists). Leave state‑dependent `rx.cond` untouched. |

## Rollback Plan

1. Revert all modified files via `git checkout -- <file>`.
2. If changes have been committed, create a revert commit: `git revert HEAD`.
3. Because the changes are purely syntactic and do not affect data persistence, rollback is immediate and safe.

## Dependencies

- None (all changes are within the existing codebase).

## Success Criteria

- [ ] `likedin` typo fixed everywhere (data, dataclass, component).
- [ ] No `rx.text.strong` remains in `info_detail.py` or `card_detail.py`.
- [ ] All static‑data `rx.cond` blocks in `info_detail.py` replaced with Python `if`.
- [ ] All views use `Size`/`EmSize` constants for spacing/padding.
- [ ] At least two repeated style patterns moved to `styles.py`.
- [ ] Layout passes visual verification on mobile and desktop viewports.