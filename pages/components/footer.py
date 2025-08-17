from re import A
import reflex as rx

# ---------- Sticky Header ----------
def footer_section() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.vstack(
                rx.image(
                    src="/Brand_image.png",
                    object_fit="contain",
                    width="150px",
                    margin_top="-30px",  
                    on_click=rx.call_script("document.querySelector('.scroll-root')?.scrollTo({ top: 0, behavior: 'smooth' });"),
                    _hover={"transform": "scale(1.1)", "transition": "transform 0.2s"},
                ),
                rx.text(
                    "Rooted in Care and Healthy Growth;\nDesigned to Ease Your Day!",
                    color="rgb(92, 94, 92)",
                    font_family="Comic Sans MS",
                    font_size=["0.5em", "0.5em", "0.8em", "0.8em"],
                    text_align="center",
                    margin_top="-40px",
                    white_space="pre-line",
                ),
                height="100px",
                spacing="1",
                align_items="center",
            ),
            rx.box(min_width="100px",display =["none", "none","flex","flex"]), #empty for spacing
            rx.hstack(
                rx.vstack(
                    rx.text("About",
                            color="rgb(0, 0, 0)",
                            font_family="Comic Sans MS",
                            font_size=["0.8em", "0.8em", "1em", "1em"],
                            ),
                    rx.link(
                            rx.text(
                                "Our Story",
                                color="rgb(92, 94, 92)",
                                font_family="Comic Sans MS",
                                _hover={"transform": "scale(1.1)", "transition": "transform 0.2s"},
                                font_size=["0.8em", "0.8em", "1em", "1em"],
                                ),
                            href="/our-story",
                            style={"textDecoration": "none", "color": "inherit"},  # looks like plain text
                            ),
                    rx.link(
                            rx.text(
                                "Survey",
                                color="rgb(92, 94, 92)",
                                font_family="Comic Sans MS",
                                _hover={"transform": "scale(1.1)", "transition": "transform 0.2s"},
                                font_size=["0.8em", "0.8em", "1em", "1em"],
                                ),
                            href="https://tally.so/r/nPqQLe",
                            is_external=True,  # adds target="_blank" rel="noopener noreferrer"
                            style={"textDecoration": "none", "color": "inherit"},  # looks like plain text
                            ),
                            align_items="left",
                            margin_top="-10px",
                        ),
                
                rx.vstack(
                    rx.text("Support",
                            color="rgb(0, 0, 0)",
                            font_family="Comic Sans MS",
                            font_size=["0.8em", "0.8em", "1em", "1em"],
                            ),
                    rx.dialog.root(
                            rx.dialog.trigger(
                                rx.text("Contact us",color="rgb(92, 94, 92)",font_family="Comic Sans MS",
                                    _hover={"transform": "scale(1.1)", "transition": "transform 0.2s"},
                                    cursor="pointer",
                                    font_size=["0.8em", "0.8em", "1em", "1em"],
                                    ),
                                              ),
                            rx.dialog.content(
                                rx.dialog.title("You can Contact us through our email"),
                                rx.dialog.description(
                                    "Care@LovePacked.ca",
                                ),
                                rx.dialog.close(
                                    rx.button("Close", size="1",margin_top="10px",),
                                ),
                            ),
                        ),
                        
                            align_items="left",
                            margin_top="-10px",
                        ),
                
                spacing="6",
                margin_top="15px",
                
            ),

            top="0",
            width="100%",
            spacing="6",
        ),
        z_index=800,
        bottom="0",
        width="100%",
        min_height="140px",
        overflow="hidden",
        padding="1em",
        background_color="rgba(248, 228, 196)",
        box_shadow="none",
    )

