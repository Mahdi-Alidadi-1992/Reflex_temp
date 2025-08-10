import reflex as rx
from pages.components.header import sticky_header
from pages.components.email_sign import email_signup_section
from pages.state.sticky_header import Sicky_Header_State

# ---------- Home Page ----------
@rx.page(route="/")   # optional; if you prefer file-based routing
def index() -> rx.Component:
    return rx.vstack(
        sticky_header(),
        email_signup_section(),
        spacing="2",
        align_items="center",
        justify_content="top",
        background_color="rgba(246, 241, 235)",
        min_height="100vh",
        width="100vw",
        height="100vh",
        overflow_x="hidden",
        overflow_y="scroll",
        on_scroll=Sicky_Header_State.update_scroll_y,
        id="my_vstack",
    )