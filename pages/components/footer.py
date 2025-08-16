import reflex as rx

# ---------- Sticky Header ----------
def footer_section() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.image(
                src="/Brand_image.png",
                object_fit="contain",
                width="170px",
                margin_top="-40px",  
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

            top="0",
            width="100%",
        ),
        bottom="0",
        width="100%",
        height="100px",
        min_height="100px",
        overflow="hidden",
        padding="1em",
        background_color="rgba(255, 245, 229)",
        box_shadow="none",
    )

