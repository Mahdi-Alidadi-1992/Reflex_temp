# pages/components/our_story.py
from functools import lru_cache
from pathlib import Path
import reflex as rx
from markdown import markdown  # pip install markdown


@lru_cache(maxsize=1)
def _read_md() -> str:
    path = Path(__file__).resolve().parents[2] / "content" / "our_story.md"
    return path.read_text(encoding="utf-8")


@lru_cache(maxsize=1)
def _md_to_html() -> str:
    # Convert once at import time; no client parsing needed.
    return markdown(_read_md(), extensions=["extra", "sane_lists", "smarty"])


# Build the heavy subtree once and reuse it (now as raw HTML).
STORY_BOX = rx.box(
    rx.html(_md_to_html()),  # <-- faster than rx.markdown for large docs
    color="rgb(92, 94, 92)",
    max_width="800px",
    width="100%",
    padding="2rem",
    margin_x="auto",
    line_height="1.75",
    font_family="Comic Sans MS",
)


def our_story_section() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Lightening your load for more bonding moments",
            font_family="Comic Sans MS",
            font_size="2em",
            color="rgb(92, 94, 92)",
            white_space="pre-wrap",     # respects your \n
        ),
        STORY_BOX,
        align_items="center",
        width="100%",
        padding="2em 2em 0 2em",
    )
