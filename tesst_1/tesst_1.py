import reflex as rx
import time

# ---------- Header App State ----------
class Header_State(rx.State):
    """The app state."""
    hero_size: int = 200
    page_scroll_y: int = 0
    def click_on_hero(self):
        """Grow then shrink the hero image on click."""
        for i in range(200, 301, 5):
            self.hero_size = i
            time.sleep(0.02)
            yield
        for i in range(300, 199, -5):
            self.hero_size = i
            time.sleep(0.02)
            yield
    
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
                rx.text("Order", font_family="Comic Sans MS", _hover={"transform": "scale(1.1)", "transition": "transform 0.2s"},),
                rx.text("How It Works", font_family="Comic Sans MS", _hover={"transform": "scale(1.1)", "transition": "transform 0.2s"},),
                rx.text("On the Menu", font_family="Comic Sans MS", _hover={"transform": "scale(1.1)", "transition": "transform 0.2s"},),
                rx.button("Sign Up / Log In", background_color="rgb(161, 169, 130)", font_family="Comic Sans MS", _hover={"transform": "scale(1.1)", "transition": "transform 0.2s"},),
                rx.image(
                    src="/Shopping Cart.png",
                    width="60px",
                    margin_top="-10px",
                     _hover={"transform": "scale(1.1)", "transition": "transform 0.2s"},
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
                src="/Yummak_Brand.png",
                object_fit="contain",
                width="200px",
                margin_top="-20px",  # Move it upward
                on_click=rx.call_script(
                    "document.getElementById('my_vstack')?.scrollTo({ top: 0, behavior: 'smooth' });"
                ),
                _hover={"transform": "scale(1.1)", "transition": "transform 0.2s"},
            ),
            rx.spacer(),
            rx.hstack(
                rx.text("Order", font_family="Comic Sans MS", _hover={"transform": "scale(1.1)", "transition": "transform 0.2s"},),
                rx.text("How It Works", font_family="Comic Sans MS", _hover={"transform": "scale(1.1)", "transition": "transform 0.2s"},),
                rx.text("On the Menu", font_family="Comic Sans MS", _hover={"transform": "scale(1.1)", "transition": "transform 0.2s"},),
                rx.button("Sign Up / Log In", background_color="rgb(161, 169, 130)", font_family="Comic Sans MS", _hover={"transform": "scale(1.1)", "transition": "transform 0.2s"},),
                rx.image(
                    src="/Shopping Cart.png",
                    width="60px",
                    margin_top="-10px",
                     _hover={"transform": "scale(1.1)", "transition": "transform 0.2s"},
                    ),
                spacing="4",
                display=["none", "none", "flex", "flex", "flex"],
                margin_top="15px",
            ),

            # Mobile Hamburger Icon
            lateral_menu(),
            top="0",
            width="100%",
        ),

        position="fixed",
        top="0",
        width="100%",
        height="80px",
        overflow="hidden",
        padding="1em",
        background_color=rx.cond(Sicky_Header_State.scroll_y > 10, "rgba(255, 242, 214, 0.7)", "transparent"),
        transition="background-color 0.1s ease",
        z_index="1000",
        box_shadow=rx.cond(Sicky_Header_State.scroll_y > 10, "0 2px 6px rgba(0,0,0,0.2)", "none"),
    )


# ---------- Header Section ----------
def header_section() -> rx.Component:
    return rx.box(
        # Background image and overlay
        rx.box(
            height="100%",
            width="100%",
            background_image="url('Header_image_2.png')",
            background_size="cover",
            background_position="center",
            opacity="0.5",
            position="absolute",
            top="0",
            left="0",
            z_index="0",
        ),
        # Hero section with text and image
        rx.box(
            rx.vstack(
                rx.flex(
                    rx.text(
                        "Welcome to Lunch Hero!",
                        size="9",
                        font_weight="bold",
                        color="white",
                        text_align="center",
                        font_family="Comic Sans MS",
                        ),
                    rx.box(

                        rx.image(
                        src="/Page_icon.png",
                        height = Header_State.hero_size,
                        width = "auto",
                        on_click = Header_State.click_on_hero,
                        z_index="1",
                        position="absolute",
                        ),
                        position="relative",
                        height="200px",     # Set fixed height for the container
                        width="200px",      # Set fixed width or adjust as needed
                    ),
                    width="100%",
                    justify_content = "center",
                    align_items = "center",
                ),
                    
                rx.text(
                    "We’re developing a convenient lunchbox service designed to take the stress out of daily school lunch prep for busy parents while making healthy eating fun and appealing for kids! "
                    "Our goal is to deliver fresh, nutritious, and allergen-aware lunches that kids genuinely enjoy; served with a playful twist to help reduce the chances of food coming back uneaten!",
                    font_size="md",
                    color="white",
                    text_align="center",
                    border_radius="10px",
                    background_color="rgba(0, 0, 0, 0.4)",
                    font_family="Comic Sans MS",
                    padding="1em",
                    margin_top="-3em",
                ),
                align_items="center",
                justify_content="center",
                
            ),
            z_index="1",
            position="relative",
            padding="1em",
            align_items="flex-start",
            justify_content="flex-start",
            height="100%",
            width="100%",
        ),
        height="fit-content", #"300px",
        width="100vw",
        position="relative",
        #overflow="hidden",
        align_items="flex-start",
    )


# ---------- Body Section ----------
def body_section() -> rx.Component:

    return rx.vstack(
        rx.input(id="First_Name", placeholder="First Name", size="3"),
        rx.input(id="Email", placeholder="Email Address", size="1"),
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
        header_section(),
        body_section(),
        align_items="center",
        justify_content="top",
        background_color="rgba(255, 246, 232,0.8)",
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
