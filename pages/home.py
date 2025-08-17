import reflex as rx
from pages.components.header import sticky_header, header_styles
from pages.components.footer import footer_section 
from pages.components.email_sign import email_signup_section
from pages.components.testimonials import testimonials_marquee
from pages.components.Survay_Section import survay_section

_IO_SCRIPT = """
(function(){
  const header = document.getElementById('lp-header');
  const scroller = document.getElementById('home_page'); // null means use window
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


# ---------- Home Page ----------
@rx.page(route="/", title="Home")   # optional; if you prefer file-based routing
def home() -> rx.Component:
    return rx.vstack(
        header_styles(),
        sticky_header(),
        survay_section(),
        email_signup_section(),
        testimonials_marquee(speed_s=60,),
        rx.spacer(),
        footer_section(),
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
        id="home_page",
        class_name="scroll-root",
    ) 