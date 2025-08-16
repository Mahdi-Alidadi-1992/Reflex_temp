import reflex as rx

# ---------- Sicky Header State ----------
class Sicky_Header_State(rx.State):
    show_drawer: bool = False
       
    def open_drawer(self):
        self.show_drawer = True
    def close_drawer(self):
        self.show_drawer = False
    