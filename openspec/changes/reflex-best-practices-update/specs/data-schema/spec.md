# Delta Spec: Data Schema

## Domain
`assets/data/data.json`, `portafolio/data.py`, `portafolio/components/media.py`

## ADDED Requirements

### Requirement: Correct LinkedIn Field Name

The system MUST use the field name `linkedin` (spelled correctly) in every layer of the data pipeline — JSON source, Python dataclass, and component reference.

The `likedin` key in `data.json` MUST be renamed to `linkedin`.
The `Media.likedin` field in `data.py` MUST be renamed to `Media.linkedin`.
The reference `data.likedin` in `media.py` MUST be updated to `data.linkedin`.
All three changes MUST be applied atomically; a partial fix SHALL be considered a broken state.

#### Scenario: JSON key is correct

- GIVEN the file `assets/data/data.json` is loaded
- WHEN the `media` object is inspected
- THEN it SHALL contain a key named `linkedin`
- AND it SHALL NOT contain a key named `likedin`

#### Scenario: Dataclass field is correct

- GIVEN the `Media` dataclass in `portafolio/data.py` is instantiated from `data.json`
- WHEN `Media(**media_dict)` is called
- THEN the instance SHALL expose attribute `linkedin`
- AND accessing `instance.likedin` SHALL raise `AttributeError`

#### Scenario: Component reads correct field

- GIVEN a `Media` instance with a valid `linkedin` URL
- WHEN the `media()` component renders
- THEN the LinkedIn `icon_button` SHALL receive the correct URL from `data.linkedin`
- AND no `AttributeError` or `KeyError` SHALL be raised at runtime
