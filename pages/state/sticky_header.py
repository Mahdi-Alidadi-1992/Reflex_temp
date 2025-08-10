import reflex as rx

# ---------- Sicky Header State ----------
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
    