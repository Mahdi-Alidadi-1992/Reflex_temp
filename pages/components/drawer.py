import reflex as rx
from pages.state.drawer_state import DrawerState

# ---------- Drawer Content ----------
 
def drawer_content():
    return rx.drawer.content(
            rx.vstack(
                rx.link(
                    rx.text(
                            "Our Story",
                            font_family="Comic Sans MS",
                            color="rgb(92, 94, 92)",
                            _hover={"transform": "scale(1.1)", "transition": "transform 0.2s"},
                        ),
                    href="/our-story",
                    style={"textDecoration": "none", "color": "inherit"},  # looks like plain text
                    on_click=DrawerState.toggle_drawer,  # <-- Close drawer on click
                ),
                rx.link(
                    rx.button("Sign Up / Log In", background_color="rgb(107, 125, 103)", font_family="Comic Sans MS", _hover={"transform": "scale(1.1)", "transition": "transform 0.2s"},),
                    href="/",
                    on_click=DrawerState.toggle_drawer,  # <-- Close drawer on click
                ),  
        ),
        on_pointer_down_outside=DrawerState.toggle_drawer,  # <-- Add this line
        top="auto",
        right="0",
        left = "auto",
        height="100%",
        width="20em",
        padding="2em",
        background_color="#FFF"
        
        
    ),

# ---------- Lateral Menu ----------

def lateral_menu():
    return rx.drawer.root(
        rx.drawer.trigger(
            rx.icon(
                "menu",
                size=40,
                color="#6b7d67",  # green
                on_click=DrawerState.toggle_drawer,
                display=["flex", "flex", "none", "none", "none"],  # Show on mobile only
                margin_top = "15px"
                    ),
        ),
        rx.drawer.overlay(on_click=DrawerState.toggle_drawer),
        rx.drawer.portal(drawer_content(),
                            
                        ), 
        open = DrawerState.is_open,     # <-- controls smooth animation
        close = ~ DrawerState.is_open,  # <-- controls smooth animation
        direction="right",
        modal=False,
        dismissible=True,    
    )
    