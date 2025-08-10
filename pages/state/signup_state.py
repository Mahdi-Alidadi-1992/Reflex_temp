import re
from sqlmodel import Field, select
from sqlalchemy import Column, String
import reflex as rx

EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+$", re.I)

class Subscriber(rx.Model, table=True):
    id: int | None = Field(default=None, primary_key=True)
    first_name: str = Field(max_length=80)
    email: str = Field(sa_column=Column(String, unique=True, index=True, nullable=False))

class SignUpState(rx.State):
    dialog_open: bool = False
    dialog_title: str = ""
    dialog_message: str = ""
    dialog_kind: str = "info"  # "success" | "error" | "info"

    @staticmethod
    def _valid_email(email: str) -> bool:
        return bool(EMAIL_REGEX.fullmatch(email or ""))

    def _open_dialog(self, title: str, message: str, kind: str = "info"):
        self.dialog_title = title
        self.dialog_message = message
        self.dialog_kind = kind
        self.dialog_open = True

    def close_dialog(self):
        self.dialog_open = False

    def submit(self, form_data: dict):
        first = (form_data.get("first_name") or "").strip()
        email = (form_data.get("email") or "").strip().lower()

        if not first:
            self._open_dialog("Missing first name", "Please enter your first name.", "error")
            return
        if not self._valid_email(email):
            self._open_dialog("Invalid email", "Please enter a valid email address.", "error")
            return

        with rx.session() as session:
            existing = session.exec(
                select(Subscriber).where(Subscriber.email == email)
            ).first()

            if existing:
                if first and existing.first_name != first:
                    existing.first_name = first
                    session.add(existing)
                    session.commit()
                self._open_dialog("You're already on the list", "No action needed ✨", "info")
                return

            session.add(Subscriber(first_name=first, email=email))
            session.commit()
            self._open_dialog("You're in!", "Thanks! You're on the list. 🎉", "success")
