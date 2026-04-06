# Delta Spec: Styling

## Domain
`portafolio/styles/styles.py`, `portafolio/components/`

## ADDED Requirements

### Requirement: Centralized Card Style Constants

Repeated style properties applied to card-like components MUST be extracted into named constants
in `portafolio/styles/styles.py`.

At minimum, TWO repeated style patterns MUST be centralized:

| Constant name | Properties it captures | Used in |
|---------------|------------------------|---------|
| `CARD_STYLE` | `width="100%"` (card full-width pattern) | `card_detail.py`, `info_detail.py` |
| `LINK_STYLE` | `text_decoration="none"`, `width="100%"` | `card_detail.py` |

- Each constant MUST be a Python `dict` keyed by Reflex style property names.
- Components that previously declared these properties inline MUST reference the constant via `**CARD_STYLE` / `**LINK_STYLE` unpacking.
- No new visual behaviour MUST be introduced; only structural consolidation is required.

#### Scenario: Card style constant is defined

- GIVEN the file `portafolio/styles/styles.py` is imported
- WHEN the module is inspected
- THEN `CARD_STYLE` MUST be a `dict` containing at minimum `{"width": "100%"}`
- AND `LINK_STYLE` MUST be a `dict` containing at minimum `{"text_decoration": "none", "width": "100%"}`

#### Scenario: card_detail references centralized styles

- GIVEN the file `portafolio/components/card_detail.py`
- WHEN the source is inspected
- THEN inline `width="100%"` on `rx.card` MUST NOT appear as a standalone keyword argument
- AND `**CARD_STYLE` or equivalent unpacking MUST be present
- AND `**LINK_STYLE` or equivalent unpacking MUST be present on `rx.link`

#### Scenario: Removing a style constant does not silently break layout

- GIVEN the constants are used via unpacking (`**CARD_STYLE`)
- WHEN `CARD_STYLE` is removed from `styles.py`
- THEN Python MUST raise a `NameError` at import time
- AND the broken state MUST be immediately visible (no silent regression)

---

### Requirement: No New Inline Style Duplication

After the centralization step, no NEW repeated inline style dictionaries with identical keys and values
MUST be introduced into any component file.
Existing single-use inline styles MAY remain if they are not duplicated elsewhere.

#### Scenario: New component follows centralized pattern

- GIVEN a developer adds a new card-like component in `portafolio/components/`
- WHEN the component defines card or link styling
- THEN it MUST import and reference `CARD_STYLE` / `LINK_STYLE` from `styles.py`
- AND MUST NOT redeclare the same properties inline
