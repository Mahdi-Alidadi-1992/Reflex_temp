import reflex as rx
from rxconfig import config
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

    def set_scroll_y(self, y: int):
        self.scroll_y = y

    @rx.event
    def update_scroll_y(self):
        return rx.call_script(
            "document.getElementById('my_vstack').scrollTop",
            callback= Sicky_Header_State.set_scroll_y,
        )

class DrawerState(rx.State):
    is_open: bool = False

    @rx.event
    def toggle_drawer(self):
        self.is_open = not self.is_open
 
def drawer_content():
    return rx.drawer.content(
        rx.vstack(
            
            rx.link("Go to Target", href="#target", on_click=DrawerState.toggle_drawer),
            rx.link("Another Option", href="#", on_click=DrawerState.toggle_drawer),
            rx.link("More Options", href="#", on_click=DrawerState.toggle_drawer),
        ),
 
        height="100%",
        width="20%",
        padding="2em",
        background_color=rx.color("grass", 7),
        on_pointer_down_outside=DrawerState.toggle_drawer,  # <-- Add this line
        
    ),
    
def lateral_menu():
    return rx.drawer.root(
        rx.drawer.trigger(
            rx.icon(
                "menu",
                size=20,
                color = rx.cond(Sicky_Header_State.scroll_y > 10, "Black", "white"),
                on_click=DrawerState.toggle_drawer,
                    ),
        ),
        rx.drawer.overlay(on_click=DrawerState.toggle_drawer),
        rx.drawer.portal(drawer_content()),
        open = DrawerState.is_open,     # <-- controls smooth animation
        close = ~ DrawerState.is_open,  # <-- controls smooth animation
        direction="left",
        modal=False,
        dismissible=True,    
    )
    
def sticky_header() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.image(
                src="/Yummak_Brand.png",
                height="auto",
                width="200px",
            ),
            rx.flex(
                rx.text("Order"),
                rx.text("How It Works"),
                rx.text("On the Menu"),
                rx.button("Sign Up / Log In "),
                 gap="5"
                ),
            gap="25"
        ),

        position="fixed",
        top="0",
        width="100%",
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
                        src="/Hero_Background.gif",
                        height = Header_State.hero_size,
                        width = "auto",
                        visibility = rx.cond(Header_State.hero_size > 200,"visible","hidden"),  # Hidden image for the hover effect
                        z_index="0",
                        position="absolute",
                        margin_top="-1em",
                        ),
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

