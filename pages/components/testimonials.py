# pages/components/testimonials.py
import reflex as rx

def style_tag(css: str) -> rx.Component:
    # Inline a <style> element safely.
    return rx.html(f"<style>{css}</style>")

# ---- Your data ----
TESTIMONIALS = [
    {"name": "Sara • Windsor", "text": "LovePacked turned lunch stress into a 2-minute task. My kids actually finish their food."},
    {"name": "Jeff • Toronto", "text": "Fresh, fun, and zero planning. We’ve cut food waste by half."},
    {"name": "Mina • Ottawa", "text": "The little stories got my picky eater to try veggies. Magic."},
    {"name": "Ava • London", "text": "It’s like someone pre-solved mornings for me."},
]

def _review_card(item: dict, width: str, aria_hidden: bool = False) -> rx.Component:
    return rx.box(
        rx.text(f"“{item['text']}”", as_="p", line_height="1.7"),
        rx.text(item["name"], color="rgb(92, 94, 92, 0.8)", size="2"),
        padding="1rem",
        border="1px solid rgba(0,0,0,0.08)",
        border_radius="14px",
        bg="white",
        box_shadow="0 6px 20px rgba(0,0,0,0.06)",
        width=width,
        flex="0 0 auto",
        role="listitem",
        aria_hidden="true" if aria_hidden else "false",
    )

def testimonials_marquee(
    speed_s: int = 36,
    card_width: str = "clamp(280px, 36vw, 360px)",
    gap: str = "1rem",
    bg: str = "#fafafa",
) -> rx.Component:
    originals = [_review_card(i, card_width) for i in TESTIMONIALS]
    clones = [_review_card(i, card_width, aria_hidden=True) for i in TESTIMONIALS]

    css = f"""
    .lp-testi-wrap {{ position: relative; overflow: hidden; }}
    .lp-testi-track {{
      display: flex;
      gap: {gap};
      width: max-content;
      animation: lp-testi-scroll {speed_s}s linear infinite;
      will-change: transform;
    }}
    .lp-testi-wrap:hover .lp-testi-track {{ animation-play-state: paused; }}
    @keyframes lp-testi-scroll {{
      0%   {{ transform: translateX(0); }}
      100% {{ transform: translateX(-50%); }}
    }}
    @media (prefers-reduced-motion: reduce) {{
      .lp-testi-track {{ animation: none; transform: none; }}
    }}
    """


    return rx.box(
        style_tag(css),

        # Edge fades
        rx.box(
            position="absolute", left="0", top="0", bottom="0", width="60px",
            style={"background": "linear-gradient(to right, var(--t-bg), rgba(250,250,250,0))"},
            pointer_events="none", z_index="1",
        ),
        rx.box(
            position="absolute", right="0", top="0", bottom="0", width="60px",
            style={"background": "linear-gradient(to left, var(--t-bg), rgba(250,250,250,0))"},
            pointer_events="none", z_index="1",
        ),

        # Moving track
        rx.box(
            rx.hstack(*(originals + clones), class_name="lp-testi-track", role="list"),
            class_name="lp-testi-wrap",
            padding_y="1rem",
        ),

        width="100%",
        bg=bg,
        padding_x="1rem",
        border_radius="16px",
        position="relative",
        style={"--t-bg": bg},
    )