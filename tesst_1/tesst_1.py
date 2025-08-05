import reflex as rx
import time


    
class Sicky_Header_State(rx.State):
    scroll_y: int = 0
    show_drawer: bool = False
    
    def set_scroll_y(self, y: int):
        self.scroll_y = y
        
    @rx.event
    def update_scroll_y(self):
        return rx.call_script(
            "document.getElementById('my_vstack').scrollTop",
            callback= Sicky_Header_State.set_scroll_y,
        )
        
    def open_drawer(self):
        self.show_drawer = True

    def close_drawer(self):
        self.show_drawer = False
    
    
class DrawerState(rx.State):
    is_open: bool = False

    @rx.event
    def toggle_drawer(self):
        self.is_open = not self.is_open
 
def drawer_content():
    return rx.drawer.content(
            rx.vstack(
                rx.text("Our Story", font_family="Comic Sans MS", _hover={"transform": "scale(1.1)", "transition": "transform 0.2s"},),
                rx.button("Sign Up / Log In", background_color="rgb(161, 169, 130)", font_family="Comic Sans MS", _hover={"transform": "scale(1.1)", "transition": "transform 0.2s"},),  
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
    
def lateral_menu():
    return rx.drawer.root(
        rx.drawer.trigger(
            rx.icon(
                "menu",
                size=40,
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
    
def sticky_header() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.image(
                src="/Brand_image.png",
                object_fit="contain",
                width="200px",
                margin_top="-40px",  # Move it upward
                on_click=rx.call_script(
                    "document.getElementById('my_vstack')?.scrollTo({ top: 0, behavior: 'smooth' });"
                ),
                _hover={"transform": "scale(1.1)", "transition": "transform 0.2s"},
            ),
            rx.spacer(),
            rx.hstack(
                rx.text("Our Story", font_family="Comic Sans MS", _hover={"transform": "scale(1.1)", "transition": "transform 0.2s"},),
                rx.button("Sign Up / Log In", background_color="rgb(159, 171, 160)", font_family="Comic Sans MS", _hover={"transform": "scale(1.1)", "transition": "transform 0.2s"},),
                spacing="4",
                display=["none", "none", "flex", "flex", "flex"],
                margin_top="15px",
            ),
            # Mobile Hamburger Icon
            lateral_menu(),
            top="0",
            width="100%",
            #align_items="center",
        ),
        position="sticky",#"fixed",
        top="0",
        width="100%",
        height="100px",
        min_height="100px",
        overflow="hidden",
        padding="1em",
        background_color=rx.cond(Sicky_Header_State.scroll_y > 10, "rgba(255, 245, 229, 0.7)", "rgba(255, 245, 229)"),
        transition="background-color 0.05s ease",
        z_index="1000",
        box_shadow=rx.cond(Sicky_Header_State.scroll_y > 10, "0 2px 6px rgba(0,0,0,0.2)", "none"),
    )

# ---------- Body Section ----------
def body_section() -> rx.Component:

    return rx.vstack(
        rx.heading("Be the first one to know", font_family="Comic Sans MS", font_size="2em", color="rgb(92, 94, 92)",),
        rx.text("About our latest product launches, parenting secrets, and more!", font_family="Comic Sans MS", font_size="1em", color="rgb(92, 94, 92, 0.5)",),
        rx.input(id="First_Name", placeholder="First Name", size="3"),
        rx.input(id="Email", placeholder="Email Address", size="3"),
        rx.button("Sign up for Early Access + Updates",
            background_color="rgb(161, 169, 130)",
            font_family="Comic Sans MS",
            _hover={"transform": "scale(1.1)", "transition": "transform 0.2s"},
            on_click=rx.call_script(
                "alert('Thank you for signing up! We will keep you updated.')"
            ),
        ),
        align_items="center",
        width="100%",
        padding="2em",
        id="target",  # Anchor for the sticky header link
    )


# ---------- Main Page ----------
def index() -> rx.Component:
    return rx.vstack(
        sticky_header(),
        body_section(),
        spacing="2",
        align_items="center",
        justify_content="top",
        background_color="rgba(246, 241, 235)",
        min_height="100vh",
        width="100vw",  # Prevents horizontal overflow
        height="100vh",  # Ensures full viewport height
        overflow_x="hidden",  # Disables horizontal scroll
        overflow_y="scroll",    # Enables vertical scroll
        on_scroll=Sicky_Header_State.update_scroll_y,
        id="my_vstack",
    )


# ---------- App Setup ----------
STYLESHEETS = ["/css/your_stylesheet.css"]
app = rx.App(stylesheets=STYLESHEETS)
app.add_page(index, title="Welcome Page")
