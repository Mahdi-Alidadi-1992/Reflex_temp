import reflex as rx

# config = rx.Config(
#     app_name="tesst_1",
#     show_built_with_reflex=False,  # <-- hide the badge
#     plugins=[rx.plugins.TailwindV3Plugin()],
#     frontend_port=3000,
#     backend_port=8000,
# )


config = rx.Config(
    app_name="tesst_1",                 # keep your app name
    # Bind backend only to localhost; Caddy is the public entrypoint
    how_built_with_reflex=False,  # <-- hide the badge
    backend_host="127.0.0.1",
    backend_port=8000,

    # Public URLs (used by the frontend to reach your backend)
    api_url="https://lovepacked.ca",
    deploy_url="https://lovepacked.ca",

    show_built_with_reflex=False,       # hide the badge
    # (optional) silence sitemap warning:
    # disable_plugins=["reflex.plugins.sitemap.SitemapPlugin"],
)