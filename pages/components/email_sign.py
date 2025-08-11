# pages/components/email_sign.py
import reflex as rx
from pages.state.signup_state import SignUpState

# ---------- Email Signup Section ----------

def email_signup_section() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Be the first one to know",
            font_family="Comic Sans MS",
            font_size="2em",
            color="rgb(92, 94, 92)",
            text_align="center",
        ),
        rx.text(
            "About our latest product launches, parenting secrets, and more!",
            font_family="Comic Sans MS",
            font_size="1em",
            color="rgb(92, 94, 92, 0.5)",
            text_align="center",
        ),

        # Responsive container: fills width, but caps to ~22rem on larger screens
        rx.box(
            rx.form(
                rx.input(
                    name="first_name",
                    placeholder="First Name",
                    font_size="1.2em",
                    width="100%",                       # 👈 fill container
                    style={"boxSizing": "border-box"},
                    class_name="brand-green",  # use class_name for CSS styles
                ),
                rx.input(
                    name="email",
                    placeholder="Email Address",
                    type="text",                         # use text + input_mode if you disabled native validation
                    input_mode="email",
                    font_size="1.2em",
                    width="100%",                       # 👈 fill container
                    style={"boxSizing": "border-box"},
                    class_name="brand-green",  # use class_name for CSS styles
                ),
                rx.button(
                    "Sign up for Early Access + Updates",
                    type="submit",
                    background_color="rgb(107, 125, 103)",
                    font_family="Comic Sans MS",
                    width="100%",                       # 👈 full-width button on mobile
                    style={"transition": "transform 0.15s ease, opacity 0.15s ease"},
                    _hover={"transform": "translateY(-1px) scale(1.03)"},
                    _active={"transform": "translateY(0) scale(0.99)", "opacity": 0.9},
                ),
                on_submit=SignUpState.submit,
                display="flex",
                flex_direction="column",
                align_items="stretch",                  # 👈 children fill width
                gap="0.75em",
                width="100%",
            ),
            width="100%",
            max_width="22rem",                          # 👈 cap on larger screens (~352px)
            margin_x="auto",                            # 👈 center on desktop/tablet
            padding_x="1rem",                           # 👈 side padding so it never touches edges
        ),

        # Dialog (already responsive with min(90vw,...))
        rx.dialog.root(
            rx.dialog.content(
                rx.vstack(
                    rx.hstack(
                        rx.cond(
                            SignUpState.dialog_kind == "success",
                            rx.text("🎉", font_size="1.8em"),
                            rx.cond(
                                SignUpState.dialog_kind == "error",
                                rx.text("⚠️", font_size="1.8em"),
                                rx.text("ℹ️", font_size="1.8em"),
                            ),
                        ),
                        rx.dialog.title(SignUpState.dialog_title),
                        align="center",
                        spacing="3",
                    ),
                    rx.dialog.description(
                        SignUpState.dialog_message,
                        style={"lineHeight": "1.6"},
                    ),
                    rx.hstack(
                        rx.dialog.close(rx.button("OK", size="3", variant="soft")),
                        justify="end",
                        width="100%",
                        style={"marginTop": "0.75em"},
                    ),
                    spacing="3",
                    width="100%",
                ),
                style={"width": "min(90vw, 680px)"},     # 👈 mobile-friendly dialog width
                padding="1.5rem",
                border_radius="1rem",
                shadow="lg",
            ),
            open=SignUpState.dialog_open,
            on_open_change=SignUpState.set_dialog_open,
        ),

        align_items="center",
        width="100%",
        padding="2em 0",  # vertical padding only; horizontal handled in box
        id="target",
    )
