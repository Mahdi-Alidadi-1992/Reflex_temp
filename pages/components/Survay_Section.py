import reflex as rx

def survay_section() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.heading(
                "Together, We Can Make Healthy Feeding Easier",
                align="center",
                margin_bottom="2em",
                font_family="Comic Sans MS",
                font_size=["1.5em", "1.5em", "2em", "2em"],
                color="rgb(92, 94, 92)",
                white_space="pre-wrap",  # respects your \n
            ),
            rx.text(
                "We’ve heard from many parents around us who feel the weight of making sure their kids eat and eat the nutrients they need to grow. From daily dinners to packing lunches for school, feeding children is tough and can feel overwhelming. We’d love to hear if this feels true for you too.",
                align="center",
                font_family="Comic Sans MS",
                font_size=["1","1","1.2em","1.2em"],
                color="rgb(84, 102, 80,0.75)",
                margin_top="-2em",
                text_align="justify",  # aligns text to both left and right
            ),
            rx.link(
                rx.button(
                "Take the 5-min survey",
                font_family="Comic Sans MS",
                background_color="rgb(159, 171, 160)",
                color="white",
                font_size=["1.2","1.2","1.5em","1.5em"],
                _hover={"transform": "scale(1.1)", "transition": "transform 0.2s"},
                ),
                href="https://tally.so/r/nPqQLe",
                is_external=True,  # adds target="_blank" rel="noopener noreferrer"
                
            ),
            align_items="center",
            width="100%",
            padding="2em 2em 0 2em",
        ),
        rx.image(
            src="/survey_pic.webp",
            width="300px",
            height="300px",
            object_fit="cover",
            border_radius="10px",
            margin_top=["1em", "1em", "none", "none"],  # responsive margin
        ),
        align_items="center",
        width="90%",
        #padding="2em 2em 0 2em",
        flex_direction=["column", "column", "row", "row"],  # responsive layout
    )