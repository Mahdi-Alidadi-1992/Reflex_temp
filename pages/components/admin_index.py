
import reflex as rx
from ..state.admin_state import AdminState

# ---------- UI ----------

def _pill(content, color: str = "gray") -> rx.Component:
    return rx.box(
        content,
        font_size="12px",
        padding="2px 8px",
        border_radius="9999px",
        bg="rgba(0,0,0,0.05)",
        border="1px solid rgba(0,0,0,0.06)",
    )


def _table_header() -> rx.Component:
    return rx.hstack(
        rx.box("ID", width="80px"),
        rx.box("First name", flex="1"),
        rx.box("Email", flex="2"),
        rx.box("Actions", width="120px", text_align="right"),
        padding="0.5rem 0.75rem",
        border_bottom="1px solid rgba(0,0,0,0.08)",
        bg="rgba(0,0,0,0.02)",
        border_top_left_radius="12px",
        border_top_right_radius="12px",
    )


def _row(r):
    # selection highlight without `.in_` (use .contains on the list Var)
    is_selected = AdminState.selected_ids.contains(r["id"])

    return rx.hstack(
        rx.box(rx.text(r["id"]), width="80px"),
        rx.box(rx.text(r["first_name"]), flex="1"),
        rx.box(rx.text(r["email"]), flex="2"),
        rx.hstack(
            rx.button(
                "Delete",
                on_click=AdminState.delete_one(r["id"]),    # no lambda
                variant="outline",
                color="red",
                size="2",
            ),
            justify="end",
            width="120px",
        ),

        padding="0.6rem 0.75rem",
        border_bottom="1px solid rgba(0,0,0,0.06)",
        cursor="pointer",
        on_click=AdminState.toggle_select(r["id"]),       # no lambda
        bg=rx.cond(is_selected, "rgba(255,59,48,0.06)", "transparent"),
        _hover={"bg": "rgba(0,0,0,0.03)"},
    )

def admin_login_view() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Admin sign in", size="6"),
            rx.text("Enter the admin password to continue.", color="gray"),
            rx.input(
                type="password",
                placeholder="Password",
                value=AdminState.password_input,
                on_change=AdminState.set_password,
                width="100%",
            ),
            rx.button(
                "Sign in",
                on_click=AdminState.login,
                width="100%",
            ),
            rx.cond(AdminState.auth_error != "", rx.text(AdminState.auth_error, color="red")),
            spacing="3",
            width="100%",
            max_width="360px",
            padding="1rem",
            border="1px solid rgba(0,0,0,0.08)",
            border_radius="14px",
            bg="white",
            box_shadow="0 6px 20px rgba(0,0,0,0.06)",
        ),
        min_height="70vh",
    )


def admin_table_view() -> rx.Component:
    return rx.vstack(
        # Top bar
        rx.hstack(
            rx.heading("Subscribers", size="6"),
            rx.spacer(),
            _pill(
                rx.cond(
                    AdminState.loading,
                    "Loading…",
                    rx.text(AdminState.rows.length(), " total"),   # <-- works on older Reflex
                )
            ),
            _pill(rx.text(AdminState.selected_ids.length(), " selected")),
            rx.button("Refresh", on_click=AdminState.load_rows, variant="soft"),
            rx.button(
                "Delete selected",
                on_click=AdminState.delete_selected,
                color="red",
                disabled=AdminState.selected_ids.length() == 0,
            ),
            rx.button("Sign out", on_click=AdminState.logout, variant="outline"),
            align="center",
            width="100%",
        ),

        rx.cond(
            AdminState.message != "",
            rx.text(AdminState.message, color="green"),
        ),

        # Table
        rx.box(
            _table_header(),
            rx.box(
                rx.foreach(AdminState.rows, _row),
                max_height="60vh",
                overflow_y="auto",
            ),
            border="1px solid rgba(0,0,0,0.08)",
            border_radius="12px",
            bg="white",
            width="100%",
        ),

        # Footer bar: select all / clear
        rx.hstack(
            rx.button("Select all (visible)", on_click=AdminState.select_all_visible, variant="soft"),
            rx.button("Clear selection", on_click=AdminState.clear_selection, variant="ghost"),
            rx.spacer(),
            rx.text("Click a row to select/deselect.", color="gray"),
            width="100%",
        ),

        spacing="4",
        width="100%",
        max_width="900px",
        on_mount=AdminState.load_rows,   # load when entering authed view
    )
