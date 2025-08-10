# pages/components/our_story.py
from pathlib import Path
import reflex as rx

# Read the file once when the module loads (cold start only).
STORY_MD = (Path(__file__).resolve().parents[2] / "content" / "our_story.md").read_text(encoding="utf-8")

# Build the heavy subtree once and reuse it.
STORY_BOX = rx.box(
    rx.markdown(STORY_MD),
    max_width="800px",
    width="100%",
    padding="2rem",
    margin_x="auto",
    line_height="1.75",
    font_family="Comic Sans MS",
)

# def our_story_section() -> rx.Component:
#     return rx.vstack(
#         rx.heading("Lightening your load for more \n bonding moments",
#                    font_family="Comic Sans MS", font_size="2em",
#                    color="rgb(92, 94, 92)"),
#         rx.image(src="Our_Story_1.webp",  # see note below
#                  object_fit="contain", width="400px",
#                  loading="lazy", decoding="async"),
#         STORY_BOX,   # reuse, don’t rebuild
#         align_items="center",
#         width="100%",
#         padding="2em 2em 0 2em",
#     )
