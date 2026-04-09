import reflex as rx
from portafolio.components.heading import heading
from portafolio.styles.styles import Size


def about(description: list) -> rx.Component:
    return rx.vstack(
        heading("Sobre mí"),
        *[rx.text(paragraph) for paragraph in description],
        spacing=Size.DEFAULT.value
    )
