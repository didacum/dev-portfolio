# Delta Spec: Component Idioms

## Domain
`portafolio/components/info_detail.py`, `portafolio/components/card_detail.py`

## ADDED Requirements

### Requirement: Use rx.strong for Bold Text

All bold text rendering MUST use `rx.strong` instead of the deprecated `rx.text.strong`.
This applies to every occurrence across all component files.

| File | Old Pattern | Required Pattern |
|------|-------------|-----------------|
| `info_detail.py` | `rx.text.strong(info.title)` | `rx.strong(info.title)` |
| `card_detail.py` | `rx.text.strong(extra.title)` | `rx.strong(extra.title)` |

#### Scenario: Bold title renders in info_detail

- GIVEN an `Info` object with a non-empty `title`
- WHEN `info_detail(info)` is rendered
- THEN the title MUST be wrapped in `rx.strong`
- AND `rx.text.strong` MUST NOT appear anywhere in `info_detail.py`

#### Scenario: Bold title renders in card_detail

- GIVEN an `Extra` object with a non-empty `title`
- WHEN `card_detail(extra)` is rendered
- THEN the title MUST be wrapped in `rx.strong`
- AND `rx.text.strong` MUST NOT appear anywhere in `card_detail.py`

---

### Requirement: Use Python if for Static Conditional Rendering

All `rx.cond` calls that guard STATIC data (values known at Python module-load time, i.e., plain strings or lists from the `Info` / `Extra` dataclasses) MUST be replaced with Python `if` expressions.
`rx.cond` MUST only be retained for conditions that depend on Reflex `State` vars evaluated at runtime.

The following `rx.cond` blocks in `info_detail.py` are static and MUST be converted:

| Guard expression | Conversion rule |
|-----------------|-----------------|
| `info.technologies` (truthy list) | `if info.technologies:` — include the `rx.flex` badge list |
| `info.url != ""` | `if info.url:` — include the URL `icon_button` |
| `info.github != ""` | `if info.github:` — include the GitHub `icon_button` |
| `info.image != ""` | `if info.image:` — include the `rx.image` |
| `info.date != ""` | `if info.date:` — include the date `rx.badge` |
| `info.certificate != ""` | `if info.certificate:` — include the certificate `icon_button` |

#### Scenario: Technologies list is present

- GIVEN an `Info` object with a non-empty `technologies` list
- WHEN `info_detail(info)` is called at component-build time
- THEN the technology badge flex MUST be included in the component tree
- AND no `rx.cond` call MUST be used to make this decision

#### Scenario: Technologies list is absent

- GIVEN an `Info` object with an empty `technologies` list
- WHEN `info_detail(info)` is called at component-build time
- THEN no technology badge flex MUST appear in the component tree
- AND the component MUST render without errors

#### Scenario: Optional URL is present

- GIVEN an `Info` object where `url` is a non-empty string
- WHEN `info_detail(info)` is called
- THEN the URL `icon_button` MUST be present in the rendered `rx.hstack`

#### Scenario: Optional URL is absent

- GIVEN an `Info` object where `url` is an empty string `""`
- WHEN `info_detail(info)` is called
- THEN no URL `icon_button` MUST appear in the `rx.hstack`

#### Scenario: Optional image is present

- GIVEN an `Info` object where `image` is a non-empty string
- WHEN `info_detail(info)` is called
- THEN `rx.image` MUST be included in the outer `rx.flex`

#### Scenario: Optional image is absent

- GIVEN an `Info` object where `image` is `""`
- WHEN `info_detail(info)` is called
- THEN no `rx.image` MUST appear in the outer `rx.flex`
