# pages/components/testimonials.py
import reflex as rx

# Inline a <style> tag (compatible with older Reflex where rx.style isn't callable).
def style_tag(css: str) -> rx.Component:
    return rx.html(f"<style>{css}</style>")

# ---- Your data ----
TESTIMONIALS = [
    {"name": "Jessika • Toronto", "text": "I hate meal prep for kiddos. I find it the most tedious task in the world. Trying to balance nutrition with what my picky eater will actually eat, and not repeating the same stuff too often is a nightmare."},
    {"name": "Amanda • Montreal", "text": "I have 3 kids, and they all eat different things for meals and snacks. Feeding them and packing lunches for school is brutal."},
    {"name": "Jason & Jenifer • Toronto", "text": "Our absolute favorite thing about summer holidays is not having to pack lunches anymore. Trying to find a variety of things that our kids like, that are healthy, and that don’t conflict with classroom allergies or make us look totally negligent is exhausting."},
    {"name": "Vicky • Guelph", "text": "Every meal is a fight. I’m so tired. Who knew the hardest part of parenting would be the never-ending meal planning, grocery shopping, cooking, and tantrums every time I try to get them to eat anything besides chicken nuggets? I hate it."},
    {"name": "Jeremy • Waterloo", "text": "It’s exhausting putting together healthy meals multiple times a day just for them to take one bite (or 0 bites)."},
    {"name": "Freda • Windsor", "text": "I started to do the “just take a bite” thing because I couldn’t stand my kid not even trying a recipe that I knew he would like."},
    {"name": "Priyanka • Brampton", "text": "And I hate people who are like, “oh, my kids just eat what we do. We don’t do special kids meals.” Like…it’s not that easy. We tried to just feed them what we eat. We tried really hard and they just wouldn’t eat it. People who don’t have picky eaters just don’t get how frustrating it is."},
    {"name": "Pandora • Toronto", "text": "I was telling another mom we all start off so brave and full of lunchbox ideas in September… and a few weeks in it’s like, welp, here’s a granola bar and vibes!"},
    {"name": "Sarah • Sarnia", "text": "My husband and I both feel that feeding kids and packing meals for school are the most annoying chores of parenting."},
]

# ---- Reusable card ----
def _review_card(item: dict, width: str, aria_hidden: bool = False) -> rx.Component:
    return rx.box(
        rx.text(f"“{item['text']}”", as_="p", line_height="1.7",color="rgb(92, 94, 92, 0.8)"),
        rx.text(item["name"], color="rgb(92, 94, 92, 0.5)", size="2"),
        padding="1rem",
        border="1px solid rgba(0,0,0,0.08)",
        border_radius="14px",
        bg="white",
        box_shadow="0 6px 20px rgba(0,0,0,0.06)",
        width=width,
        flex="0 0 auto",           # fixed card width inside the track
        role="listitem",
        aria_hidden="true" if aria_hidden else "false",
    )

def testimonials_marquee(
    speed_s: int = 36,
    card_width: str = "clamp(280px, 36vw, 360px)",
    gap: str = "1rem",
    bg: str = "rgb(255, 245, 229)",      # solid background color
    border_radius: str = "16px",
    items: list[dict] | None = None,     # optional custom list
) -> rx.Component:
    data = items or TESTIMONIALS
    originals = [_review_card(i, card_width) for i in data]
    clones    = [_review_card(i, card_width, aria_hidden=True) for i in data]

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

        # Edge fades (use CSS var so fades match the background color)
        rx.box(
            position="absolute", left="0", top="0", bottom="0", width="60px",
            style={"background": "linear-gradient(to right, var(--t-bg), rgba(0,0,0,0))"},
            pointer_events="none", z_index="1", border_radius=border_radius,
        ),
        rx.box(
            position="absolute", right="0", top="0", bottom="0", width="60px",
            style={"background": "linear-gradient(to left, var(--t-bg), rgba(0,0,0,0))"},
            pointer_events="none", z_index="1", border_radius=border_radius,
        ),

        # Moving track
        rx.box(
            rx.hstack(*(originals + clones), class_name="lp-testi-track", role="list"),
            class_name="lp-testi-wrap",
            padding_y="1rem",
        ),

        width="100%",
        padding_x="1rem",
        bg=bg,                         # solid color (no images)
        border_radius=border_radius,
        position="relative",
        style={"--t-bg": bg},          # used by the fades above
        margin_top="2rem",
    )
