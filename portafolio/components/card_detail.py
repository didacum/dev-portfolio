import reflex as rx
from portafolio.data import Extra

from portafolio.styles.styles import IMAGE_HEIGHT, Size, CARD_STYLE, LINK_STYLE


def card_detail(extra: Extra) -> rx.Component:
    return rx.link(
        rx.card(
            rx.inset(
                rx.image(
                    src=extra.image,
                    height=IMAGE_HEIGHT,
                    width="100%",
                    object_fit="cover"
                ),
                pb=Size.DEFAULT.value
            ),
            rx.text.strong(extra.title),
            rx.text(
                extra.description,
                size=Size.SMALL.value,
                color_scheme="gray"
            ),
            **CARD_STYLE,
        ),
        href=extra.url,
        is_external=True,
        **LINK_STYLE,
    )
