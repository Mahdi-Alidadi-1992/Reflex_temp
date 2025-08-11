import reflex as rx
from pages.components.header import sticky_header
from pages.components.our_story import our_story_section
from pages.state.sticky_header import Sicky_Header_State

# ---------- our_story page ----------
@rx.page(route="/our-story", title="Our Story")   
def our_story() -> rx.Component:
    return rx.vstack(
        sticky_header(),
        our_story_section(),
        spacing="2",
        align_items="center",
        justify_content="top",
        background_color="rgba(255, 255, 255)",
        min_height="100vh",
        width="100vw",
        height="100vh",
        overflow_x="hidden",
        overflow_y="scroll",
        #on_scroll=Sicky_Header_State.update_scroll_y,
        id="our_story",
        class_name="scroll-root",
        
    ) 