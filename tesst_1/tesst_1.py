import reflex as rx
from pages import home, our_story, admin  # thanks to pages/__init__.py


# ---------- App Setup ----------
STYLESHEETS = ["/css/your_stylesheet.css"]
app = rx.App(stylesheets=STYLESHEETS)
#app.add_page(home, title="Welcome Page")
#app.add_page(our_story, )
