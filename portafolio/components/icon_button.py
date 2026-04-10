import reflex as rx


def icon_button(icon: str, url: str, text="", solid=False, color_scheme: str = None) -> rx.Component:
    btn_props = {"color_scheme": color_scheme} if color_scheme else {}
    return rx.link(
        rx.button(
            rx.icon(icon),
            text,
            variant="solid" if solid else "surface",
            **btn_props
        ),
        href=url,
        is_external=True
    )
