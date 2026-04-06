# Delta Spec: Responsiveness

## Domain
`portafolio/portafolio.py`, `portafolio/views/*.py`

## ADDED Requirements

### Requirement: Responsive Padding in Main Layout

The main layout in `portafolio.py` MUST use responsive list values for `padding_x` and `padding_y`
so that the portfolio renders comfortably on both mobile (< 640 px) and desktop (≥ 640 px) viewports.

- `padding_x` MUST use a list of at least two breakpoint values (mobile, desktop).
- `padding_y` MUST use a list of at least two breakpoint values (mobile, desktop).
- Values MUST be drawn from the existing `Size` or `EmSize` enums; hard-coded pixel strings are MUST NOT be introduced.

| Property | Current (single value) | Required (responsive list) |
|----------|----------------------|---------------------------|
| `padding_x` | `EmSize.MEDIUM.value` | `[Size.DEFAULT.value, EmSize.MEDIUM.value]` or equivalent |
| `padding_y` | `EmSize.BIG.value` | `[EmSize.MEDIUM.value, EmSize.BIG.value]` or equivalent |

#### Scenario: Mobile padding is reduced

- GIVEN a viewport width below 640 px
- WHEN the portfolio index page is rendered
- THEN the main `rx.vstack` MUST apply the first value in the `padding_x` / `padding_y` lists (smaller value)

#### Scenario: Desktop padding is full

- GIVEN a viewport width of 640 px or greater
- WHEN the portfolio index page is rendered
- THEN the main `rx.vstack` MUST apply the second value in the `padding_x` / `padding_y` lists (larger value)

---

### Requirement: Responsive Spacing in View Components

Each view component in `portafolio/views/` MUST expose consistent responsive spacing so that
section gaps are appropriate on both mobile and desktop.

The following views MUST be audited and updated where a single fixed `spacing` value is used
but a responsive list would improve the layout:

| View | Property to audit |
|------|------------------|
| `header.py` | outer `rx.hstack` `spacing` |
| `about.py` | `rx.vstack` `spacing` |
| `info.py` | outer and inner `rx.vstack` `spacing` |
| `tech_stack.py` | `rx.flex` `spacing` |
| `extra.py` | outer `rx.vstack` `spacing` |
| `footer.py` | `rx.vstack` `spacing` |

Where a responsive spacing list is warranted, values MUST follow the pattern
`[Size.SMALL.value, Size.DEFAULT.value]` (mobile first), using existing `Size` enum constants.
A view with already-correct responsive behaviour SHOULD be left unchanged.

#### Scenario: Section gap is smaller on mobile

- GIVEN any view component that has been updated with a responsive spacing list
- WHEN rendered on a viewport narrower than 640 px
- THEN the smaller (first) spacing value MUST be applied between child elements

#### Scenario: Section gap is larger on desktop

- GIVEN any view component that has been updated with a responsive spacing list
- WHEN rendered on a viewport of 640 px or wider
- THEN the larger (second) spacing value MUST be applied between child elements

#### Scenario: Views with existing responsive behaviour are unchanged

- GIVEN `extra.py`, which already uses `rx.breakpoints` for `display`
- WHEN the responsiveness audit is performed
- THEN its existing `display` logic MUST be preserved and MUST NOT be overwritten
