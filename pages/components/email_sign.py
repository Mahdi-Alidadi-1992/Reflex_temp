import reflex as rx

# ---------- Email Signup Section ----------
def email_signup_section() -> rx.Component:

    return rx.vstack(
        rx.heading("Be the first one to know", font_family="Comic Sans MS", font_size="2em", color="rgb(92, 94, 92)",),
        rx.text("About our latest product launches, parenting secrets, and more!", font_family="Comic Sans MS", font_size="1em", color="rgb(92, 94, 92, 0.5)",),
        rx.input(id="First_Name", placeholder="First Name", font_size="1.2em", width="20em",),
        rx.input(id="Email", placeholder="Email Address", font_size="1.2em", width="20em",),
        rx.button("Sign up for Early Access + Updates",
            background_color="rgb(161, 169, 130)",
            font_family="Comic Sans MS",
            _hover={"transform": "scale(1.1)", "transition": "transform 0.2s"},
            on_click=rx.call_script(
                "alert('Thank you for signing up! We will keep you updated.')"
            ),
        ),
        rx.text("by clicking sign up, you agree to our terms of service and privacy policy.", font_family="Comic Sans MS", font_size="0.8em", color="rgb(92, 94, 92, 0.5)",),
        align_items="center",
        width="100%",
        padding="2em",
        id="target",  # Anchor for the sticky header link
    )

