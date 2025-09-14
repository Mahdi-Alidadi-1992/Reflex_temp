from functools import lru_cache
from pathlib import Path
import reflex as rx
from markdown import markdown  # pip install markdown


@lru_cache(maxsize=1)
def _read_md() -> str:
    path = Path(__file__).resolve().parents[2] / "content" / "survey.md"
    return path.read_text(encoding="utf-8")


@lru_cache(maxsize=1)
def _md_to_html() -> str:
    # Convert once at import time; no client parsing needed.
    return markdown(_read_md(), extensions=["extra", "sane_lists", "smarty"])

# Build the heavy subtree once and reuse it (now as raw HTML).
Text_BOX = rx.box(
    rx.html(_md_to_html()),  # <-- faster than rx.markdown for large docs
    color="rgb(92, 94, 92)",
    max_width="500px",
    width="100%",
    margin_x="auto",
    line_height="1.75",
    font_family="'Nunito', system-ui, -apple-system, 'Segoe UI', Roboto, Arial, sans-serif",
    font_weight="400",
    text_align="Justify-lower",
    font_size=["1em", "1em", "1.2em", "1.2em"],
    margin_top="-2em"
)

def survay_section() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.heading(
                "Together, We Can Make Healthy Feeding Easier",
                align="center",
                margin_bottom="2em",
                font_family="'Nunito', system-ui, -apple-system, 'Segoe UI', Roboto, Arial, sans-serif",
                font_weight="600",
                font_size=["1.5em", "1.5em", "2em", "2em"],
                color="rgb(92, 94, 92)",
                white_space="pre-wrap",  # respects your \n
                line_height="1.5",
            ),
            rx.link(
                rx.button(
                "Take the 5-min survey",
                font_family="'Nunito', system-ui, -apple-system, 'Segoe UI', Roboto, Arial, sans-serif",
                font_weight="600",
                background_color="rgb(159, 171, 160)",
                color="white",
                font_size=["1em","1em","1.2em","1.2em"],
                _hover={"transform": "scale(1.1)", "transition": "transform 0.2s"},
                margin_top="-3em",
                size = "3"
                ),
                href="https://tally.so/r/nPqQLe",
                is_external=True,  # adds target="_blank" rel="noopener noreferrer"
                
            ),
            Text_BOX,
            
            
            align_items="center",
            width="100%",
            padding="2em 2em 0 2em",
        ),
        rx.vstack(
            rx.box(min_height="150px", display = ["None","None","None","block"]),  # Placeholder for responsive height
            rx.image(
                    src="/survey_pic.webp",
                    width=["1000px","1000px","500px","1000px"],
                    #height="500px",
                    object_fit="cover",
                    border_radius="10px",
                    margin_top=["1em", "1em", "none", "none"],  # responsive margin
                    ),
                    display = ["None","None","block","block"],
                  ),
        
        align_items="center",
        width="90%",
        flex_direction=["column", "column", "column", "row"],  # responsive layout
        margin_top=["0em","0em","0em","-3em","-4em","-5em"],
    )