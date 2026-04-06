# Design: reflex-best-practices-update

## Technical Approach

Pure refactoring pass across 7 files. No new routes, no state, no reactive data — all changes are build-time transformations: a typo rename propagated atomically across three layers, static-conditional idiom replacement, responsive padding via lists, and style constant extraction. No migration, no feature flags.

---

## Architecture Decisions

| # | Option A | Option B | Decision |
|---|----------|----------|----------|
| 1 — LinkedIn rename order | Rename in code first, JSON last | Rename data.json → data.py → media.py | **B** — JSON is the source of truth; downstream code must always match the schema. Reverse order causes runtime AttributeError during the window between commits. |
| 2 — rx.cond replacement | Keep rx.cond, update arg style | Replace with Python `if` at component-build time | **B** — `info.technologies / url / github / image / date / certificate` are all build-time constants (loaded from JSON, not State). rx.cond is correct only for reactive State vars. Using `if` produces leaner component trees and removes the cognitive burden of distinguishing reactive vs static guards. |
| 3 — Responsive values | Pass EmSize enum directly | Pass lists `[mobile_val, desktop_val]` | **B** — Reflex documents that padding/spacing props accept responsive lists natively. No new abstraction needed; values stay typed via enums. |
| 4 — Style constants location | Inline dict per call site | CARD_STYLE / LINK_STYLE dicts in styles.py | **B** — Single source of truth, consistent with BASE_STYLE already in styles.py. Unpacking `**CARD_STYLE` at call site keeps component signatures readable. |
| 5 — rx.text.strong → rx.strong | Wrapper component | Direct replacement | **Direct replacement** — rx.strong is a first-class Radix component in Reflex 0.8+. rx.text.strong is a sub-component alias that may not survive version bumps. |

---

## Data Flow

```
assets/data/data.json          ← rename "likedin" → "linkedin"
        │
        ▼
portafolio/data.py             ← Media.likedin → Media.linkedin (dataclass field)
        │
        ▼
portafolio/components/media.py ← data.likedin → data.linkedin (call site)
```

For style constants:
```
portafolio/styles/styles.py    ← add CARD_STYLE, LINK_STYLE dicts
        │
        ▼ (import + unpack)
portafolio/components/card_detail.py
```

For responsive padding:
```
portafolio/styles/styles.py    ← EmSize / Size enums (unchanged, referenced)
        │
        ▼
portafolio/portafolio.py       ← padding_x=[EmSize.SMALL.value, EmSize.MEDIUM.value]
                                   padding_y=[EmSize.MEDIUM.value, EmSize.BIG.value]
portafolio/views/info.py       ← spacing=[Size.SMALL.value, Size.DEFAULT.value]
portafolio/views/tech_stack.py ← spacing=[Size.SMALL.value, Size.DEFAULT.value]
portafolio/views/about.py      ← spacing=[Size.SMALL.value, Size.DEFAULT.value]
portafolio/views/footer.py     ← spacing=[Size.ZERO.value, Size.SMALL.value]
```

---

## File Changes

| File | Action | Description |
|------|--------|-------------|
| `assets/data/data.json` | Modify | Rename key `"likedin"` → `"linkedin"` in media object (line 13) |
| `portafolio/data.py` | Modify | Rename `Media.likedin: str` → `Media.linkedin: str` |
| `portafolio/components/media.py` | Modify | `data.likedin` → `data.linkedin` at icon_button call site |
| `portafolio/components/info_detail.py` | Modify | (1) `rx.text.strong` → `rx.strong`; (2) 6× `rx.cond` → Python `if` guards |
| `portafolio/components/card_detail.py` | Modify | (1) `rx.text.strong` → `rx.strong`; (2) replace inline width/text_decoration with `**CARD_STYLE` / `**LINK_STYLE` |
| `portafolio/styles/styles.py` | Modify | Add `CARD_STYLE = {"width": "100%"}` and `LINK_STYLE = {"text_decoration": "none", "width": "100%"}` |
| `portafolio/portafolio.py` | Modify | `padding_x` and `padding_y` → responsive lists |
| `portafolio/views/info.py` | Modify | outer `spacing` → responsive list |
| `portafolio/views/tech_stack.py` | Modify | outer `spacing` → responsive list |
| `portafolio/views/about.py` | Modify | add `spacing` responsive list to vstack |
| `portafolio/views/footer.py` | Modify | `spacing` → responsive list |

No files created. No files deleted.

---

## Interfaces / Contracts

```python
# styles.py additions
CARD_STYLE: dict = {"width": "100%"}
LINK_STYLE: dict = {"text_decoration": "none", "width": "100%"}

# data.py — Media dataclass after rename
@dataclass
class Media:
    email: str
    cv: str
    github: str
    linkedin: str          # was: likedin

# info_detail.py — Python if pattern (representative)
# BEFORE (rx.cond — wrong for static data):
rx.cond(
    info.technologies,
    rx.flex(*[rx.badge(...) for technology in info.technologies], ...)
)

# AFTER (Python if — correct for build-time constants):
*(
    [rx.flex(*[rx.badge(...) for technology in info.technologies], ...)]
    if info.technologies else []
),

# portafolio.py — responsive padding pattern
padding_x=[EmSize.SMALL.value, EmSize.MEDIUM.value],
padding_y=[EmSize.MEDIUM.value, EmSize.BIG.value],
```

---

## Testing Strategy

| Layer | What to Test | Approach |
|-------|-------------|----------|
| Static / import | `Media.linkedin` accessible; `Media.likedin` raises `AttributeError` | Python import + getattr assertion |
| Render smoke | `reflex run` starts without error; no NameError on styles | Manual: `reflex run`, check browser console |
| Visual — responsive | Mobile (<640 px): reduced padding; Desktop: full padding | Browser DevTools responsive mode |
| Visual — bold | `rx.strong` renders bold in `info_detail` and `card_detail` | Visual inspection |
| Style constants | `CARD_STYLE` / `LINK_STYLE` imported in `card_detail` without error | Import test |

---

## Migration / Rollout

No migration required. Data is static JSON loaded at startup. The rename is completed atomically within one commit per the file-update sequence documented in the Data Flow section above.

---

## Open Questions

- None. All decisions are resolved by spec requirements and existing codebase patterns.
