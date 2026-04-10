import reflex as rx

from portafolio.styles.styles import EmSize


def icon_badge(icon: str, color_scheme: str = "gray") -> rx.Component:
    return rx.badge(
        rx.icon(
            icon,
            size=32
        ),
        aspect_ratio="1",
        color_scheme=color_scheme
    )
