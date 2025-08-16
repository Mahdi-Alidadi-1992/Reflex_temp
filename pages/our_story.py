import reflex as rx
from pages.components.header import sticky_header, header_styles
from pages.components.footer import footer_section
from pages.components.our_story import our_story_section
from pages.state.sticky_header import Sicky_Header_State

_IO_SCRIPT = """
(function(){
  const header = document.getElementById('lp-header');
  const scroller = document.getElementById('our_story'); // null means use window
  // A 1px sentinel right under the header
  let sentinel = document.getElementById('lp-sentinel');
  if (!sentinel) {
    sentinel = document.createElement('div');
    sentinel.id = 'lp-sentinel';
    sentinel.style.height = '1px';
    const parent = scroller || document.body;
    (scroller ? scroller : document.body).insertBefore(
      sentinel,
      (scroller ? scroller.firstChild : document.body.firstChild)
    );
  }
  const opts = scroller ? {root: scroller, threshold: [1]} : {threshold: [1]};
  const io = new IntersectionObserver(([entry]) => {
    // Less than fully visible => page has scrolled
    header && header.classList.toggle('is-scrolled', entry.intersectionRatio < 1);
  }, opts);
  io.observe(sentinel);
})();
"""

# ---------- our_story page ----------
@rx.page(route="/our-story", title="Our Story")   
def our_story() -> rx.Component:
    return rx.vstack(
        header_styles(),
        sticky_header(),
        our_story_section(),
        rx.spacer(),
        footer_section(),  # Uncomment if you want to include the footer
        spacing="2",
        align_items="center",
        justify_content="top",
        background_color="rgba(255, 255, 255)",
        min_height="100vh",
        width="100vw",
        height="100vh",
        overflow_x="hidden",
        overflow_y="scroll",
        on_mount=rx.call_script(_IO_SCRIPT),
        id="our_story",
        class_name="scroll-root",
        
    ) 