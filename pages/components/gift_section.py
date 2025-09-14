from functools import lru_cache
from pathlib import Path
import reflex as rx
from markdown import markdown  # pip install markdown


@lru_cache(maxsize=1)
def _read_md() -> str:
    path = Path(__file__).resolve().parents[2] / "content" / "gift_section.md"
    return path.read_text(encoding="utf-8")


@lru_cache(maxsize=1)
def _md_to_html() -> str:
    # Convert once at import time; no client parsing needed.
    return markdown(_read_md(), extensions=["extra", "sane_lists", "smarty"])

# Build the heavy subtree once and reuse it (now as raw HTML).
Text_BOX = rx.box(
    rx.html(_md_to_html()),  # <-- faster than rx.markdown for large docs
    color="rgb(92, 94, 92)",
    max_width=["500px","500px","500px","800px"],
    width="100%",
    margin_x="auto",
    line_height="1.75",
    font_family="'Nunito', system-ui, -apple-system, 'Segoe UI', Roboto, Arial, sans-serif",
    font_weight="400",
    text_align="Justify",
    font_size=["1em", "1em", "1.2em", "1.2em"],
    padding=["0em 0em 0em 2em", "0em 0em 0em 2em", "0em 0em 0em 0em", "0em 0em 0em 0em"],
    
)

def gift_section() -> rx.Component:
    return rx.flex(
        rx.image(
                    src="/gift_section_pic.webp",
                    width=["800px","1000px","800px","1000px"],
                    object_fit="cover",
                    margin_top=["1em", "1em", "none", "none"],  # responsive margin
                    left="0",
                    ),
        rx.vstack(
            rx.image(
                src="/heart_pic.webp",
                width="150px",
                height="Auto",
                margin_top=["-2em","-4em","-3em","-4em"],
                align_self="start",
                margin_left=["15em","20em","0em","0em"],
            ),
            Text_BOX,
            rx.link(
                rx.button(
                "Take the 5-min survey",
                font_family="'Nunito', system-ui, -apple-system, 'Segoe UI', Roboto, Arial, sans-serif",
                font_weight="600",
                background_color="rgb(159, 171, 160)",
                color="white",
                font_size=["1em","1em","1.2em","1.2em"],
                _hover={"transform": "scale(1.1)", "transition": "transform 0.2s"},
                size = "3",
                margin_top="1em",
                
                ),
                href="https://tally.so/r/nPqQLe",
                is_external=True,  # adds target="_blank" rel="noopener noreferrer"
                padding=["0em 0em 0em 2em", "0em 0em 0em 2em", "0em 0em 0em 0em", "0em 0em 0em 0em"],    
                ),
            align_items="center",
            ),
        
        
        align_items="center",
        width="100%",
        padding=["2em 2em 2em 2em","2em 2em 0em 0em","2em 2em 0em 0em","2em 2em 0em 0em"],
        flex_direction=["column-reverse", "column-reverse", "column-reverse", "row"],  # responsive layout
        left ="0",
        margin_top=["0em","1em","0em","-3em"],
        
    )