import reflex as rx
from pages.components.admin_index import admin_table_view, admin_login_view
from pages.components.header import header_styles  # optional, reuse your styles if you like
from pages.state.admin_state import AdminState

@rx.page(route="/admin", title="Admin")
def admin() -> rx.Component:
    return rx.box(
        header_styles() if 'header_styles' in globals() else rx.fragment(),  # optional
        rx.center(
            rx.cond(
                AdminState.is_authed,
                admin_table_view(),
                admin_login_view(),
            ),
            width="100%",
        ),
        padding="1.5rem",
        min_height="100vh",
        bg="#fafafa",
    )