import reflex as rx

def survay_section() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Join Parents Like You in Making Feeding Kids Healthy Easier",
            align="center",
            margin_bottom="1em",
            font_family="Comic Sans MS",
            font_size="2em",
            color="rgb(92, 94, 92)",
            white_space="pre-wrap",  # respects your \n
        ),
        rx.text(
            "We’ve heard from many parents around us who feel the weight of making sure their kids eat and eat the nutrients they need to grow. From daily dinners to packing lunches for school, feeding children is tough and can feel overwhelming. We’d love to hear if this feels true for you too.",
            align="center",
            font_family="Comic Sans MS",
            font_size="1.2em",
            color="rgb(92, 94, 92)",
        ),
        rx.link(
            rx.button(
            "Take the 5 min survey",
            font_family="Comic Sans MS",
            background_color="rgb(107, 125, 103)",
            color="white",
            _hover={"transform": "scale(1.1)", "transition": "transform 0.2s"},
            ),
            href="https://tally.so/r/nPqQLe",
            is_external=True,  # adds target="_blank" rel="noopener noreferrer"
        ),
        align_items="center",
        width="100%",
        padding="2em 2em 0 2em",
    )