# pages/admin.py
import os
from typing import List, Dict

import reflex as rx
from sqlmodel import select

#from .components import header_styles  # optional, reuse your styles if you like
from ..state.signup_state import Subscriber        # or adjust the import to where Subscriber lives

# ---- Config ----
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "")


# ---- Admin State ----
class AdminState(rx.State):
    # Auth
    is_authed: bool = False
    password_input: str = ""
    auth_error: str = ""

    # Data & UI
    rows: List[Dict] = []       # [{"id": 1, "first_name": "...", "email": "..."}]
    selected_ids: List[int] = []
    loading: bool = False
    message: str = ""           # simple flash

    # ----- Auth -----
    def set_password(self, v: str):
        self.password_input = v

    def login(self):
        self.auth_error = ""
        if not ADMIN_PASSWORD:
            self.auth_error = "ADMIN_PASSWORD is not configured on the server."
            return
        if self.password_input == ADMIN_PASSWORD:
            self.is_authed = True
            self.password_input = ""
            # Immediately load data
            return self.load_rows()
        else:
            self.auth_error = "Incorrect password."

    def logout(self):
        self.is_authed = False
        self.password_input = ""
        self.rows = []
        self.selected_ids = []
        self.message = ""

    # ----- Data loading -----
    def load_rows(self):
        if not self.is_authed:
            return
        self.loading = True
        with rx.session() as session:
            subs = session.exec(
                select(Subscriber).order_by(Subscriber.id.desc())
            ).all()
            self.rows = [
                {"id": s.id, "first_name": s.first_name, "email": s.email}
                for s in subs
            ]
        self.loading = False
        # Clear selection if any ids vanished
        self.selected_ids = [i for i in self.selected_ids if any(r["id"] == i for r in self.rows)]

    # ----- Selection -----
    def toggle_select(self, row_id: int):
        if row_id in self.selected_ids:
            self.selected_ids = [i for i in self.selected_ids if i != row_id]
        else:
            self.selected_ids = self.selected_ids + [row_id]

    def clear_selection(self):
        self.selected_ids = []

    def select_all_visible(self):
        ids = [r["id"] for r in self.rows]
        # if all visible already selected -> clear; else select all
        if set(self.selected_ids) >= set(ids):
            self.selected_ids = []
        else:
            self.selected_ids = ids

    # ----- Delete -----
    def delete_selected(self):
        if not self.is_authed or not self.selected_ids:
            return
        with rx.session() as session:
            for rid in self.selected_ids:
                sub = session.get(Subscriber, rid)
                if sub:
                    session.delete(sub)
            session.commit()
        self.message = f"Deleted {len(self.selected_ids)} subscriber(s)."
        self.selected_ids = []
        return self.load_rows()

    def delete_one(self, row_id: int):
        if not self.is_authed:
            return
        with rx.session() as session:
            sub = session.get(Subscriber, row_id)
            if sub:
                session.delete(sub)
                session.commit()
        self.message = "Deleted 1 subscriber."
        return self.load_rows()

    # Optional: confirm delete using a browser confirm() before server action
    @rx.event
    def confirm_delete_selected(self):
        return rx.call_script(
            "window.confirm('Delete selected subscriber(s)?')",
            callback=AdminState._confirm_delete_selected_done,
        )

    def _confirm_delete_selected_done(self, ok: bool):
        if ok:
            return self.delete_selected()
