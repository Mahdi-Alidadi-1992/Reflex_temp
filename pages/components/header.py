import reflex as rx
from pages.state.sticky_header import Sicky_Header_State
from pages.components.drawer import lateral_menu

# ---------- Sticky Header ----------
def sticky_header() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.image(
                src="/Brand_image.png",
                object_fit="contain",
                width="170px",
                margin_top="-40px",  # Move it upward
                # on_click=rx.call_script(
                #     "document.getElementById('my_vstack')?.scrollTo({ top: 0, behavior: 'smooth' });"
                # ),
                on_click=rx.call_script("document.querySelector('.scroll-root')?.scrollTo({ top: 0, behavior: 'smooth' });"),
                _hover={"transform": "scale(1.1)", "transition": "transform 0.2s"},
            ),
            rx.spacer(),
            rx.hstack(
                rx.link(
                rx.text(
                        "Our Story",
                        color="rgb(92, 94, 92)",
                        font_family="Comic Sans MS",
                        _hover={"transform": "scale(1.1)", "transition": "transform 0.2s"},
                    ),
                    href="/our-story",
                    style={"textDecoration": "none", "color": "inherit"},  # looks like plain text
                ),
                rx.link(
                    rx.button("Sign Up / Log In", background_color="rgb(107, 125, 103)", font_family="Comic Sans MS", _hover={"transform": "scale(1.1)", "transition": "transform 0.2s"},),
                    href="/",
                ),
                spacing="4",
                display=["none", "none", "flex", "flex", "flex"],
                margin_top="15px",
            ),
            # Mobile Hamburger Icon
            lateral_menu(),
            top="0",
            width="100%",
            #align_items="center",
        ),
        position="sticky",#"fixed",
        top="0",
        width="100%",
        height="100px",
        min_height="100px",
        overflow="hidden",
        padding="1em",
        background_color=rx.cond(Sicky_Header_State.scroll_y > 10, "rgba(255, 245, 229, 0.7)", "rgba(255, 245, 229)"),
        transition="background-color 0.05s ease",
        z_index="1000",
        box_shadow=rx.cond(Sicky_Header_State.scroll_y > 10, "0 2px 6px rgba(0,0,0,0.2)", "none"),
    )

