import reflex as rx
from portafolio.components.card_detail import card_detail
from portafolio.components.heading import heading
from portafolio.data import Extra
from portafolio.styles.styles import Size


def extra(extras: list[Extra]) -> rx.Component:
    return rx.vstack(
        heading("Extra"),
        rx.vstack(
            *[
                card_detail(extra)
                for extra in extras
            ],
            spacing=Size.DEFAULT.value,
            display=rx.breakpoints(initial="flex", sm="none"),
            width="100%"
        ),
        rx.grid(
            *[
                card_detail(extra)
                for extra in extras
            ],
            spacing=Size.DEFAULT.value,
            columns="3",
            display=rx.breakpoints(initial="none", sm="grid"),
            width="100%"
        ),
        spacing=Size.DEFAULT.value,
        width="100%"
    )
