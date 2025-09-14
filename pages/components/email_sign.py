# pages/components/email_sign.py
import dis
import reflex as rx
from pages.state.signup_state import SignUpState

# ---------- Email Signup Section ----------

def email_signup_section() -> rx.Component:
    return rx.vstack(
            rx.heading(
                "Be the first one to know",
                font_family="'Nunito', system-ui, -apple-system, 'Segoe UI', Roboto, Arial, sans-serif",
                font_weight="600",
                font_size=["1.5em", "1.5em", "2em", "2em"],
                color="rgb(92, 94, 92)",
                text_align="center",
            ),
            rx.text(
                "Sign up to get updates and play a part in shaping healthier, easier mealtimes for parents.",
                font_family="'Nunito', system-ui, -apple-system, 'Segoe UI', Roboto, Arial, sans-serif",
                font_weight="400",
                font_size=["1","1","1.2em","1.2em"],
                color="rgb(84, 102, 80,0.75)",
                text_align="center",
                max_width="450px",  # 👈 max width for readability
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
                        "Sign up",
                        type="submit",
                        white_space="nowrap",              # 👈 don't wrap to a second line
                        font_size="1.2em",                  # 👈 consistent font size
                        background_color="rgb(159, 171, 160)",
                        font_family="'Nunito', system-ui, -apple-system, 'Segoe UI', Roboto, Arial, sans-serif",
                        font_weight="600",
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
            id="Sing_Up",#"target",
        ),
