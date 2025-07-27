import reflex as rx

config = rx.Config(
    app_name="tesst_1",
    plugins=[rx.plugins.TailwindV3Plugin()],
    frontend_port=3000,
    backend_port=8000,
)