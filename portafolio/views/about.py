import reflex as rx
from portafolio.components.heading import heading
from portafolio.styles.styles import Size


def about(description: str) -> rx.Component:
    return rx.vstack(
        heading("Sobre mí"),
        rx.text(description),
        spacing=[Size.SMALL.value, Size.DEFAULT.value]
    )
