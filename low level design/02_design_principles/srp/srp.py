"""Single Responsibility Principle (SRP): Decomposing a God Class into focused collaborators."""

from dataclasses import dataclass
from typing import Dict


# -------------------------------------------------------------
# Anti-Pattern: God Class (Violates SRP)
# -------------------------------------------------------------
class UserManagerGodClass:
    def __init__(self, username: str, email: str) -> None:
        self.username = username
        self.email = email

    # 1. Domain logic
    def update_email(self, new_email: str) -> None:
        self.email = new_email

    # 2. Persistence responsibility
    def save_to_database(self) -> None:
        print(f"[DB] INSERT INTO users (username, email) VALUES ('{self.username}', '{self.email}');")

    # 3. Notification responsibility
    def send_welcome_email(self) -> None:
        print(f"[SMTP] Sending welcome email to {self.email} via port 587...")

    # 4. Reporting responsibility
    def generate_activity_pdf(self) -> str:
        return f"PDF report binary content for {self.username}"


# -------------------------------------------------------------
# Clean Refactor: SRP Compliant Components
# -------------------------------------------------------------
@dataclass
class User:
    """1. Single Responsibility: Holds core domain state."""
    username: str
    email: str


class UserRepository:
    """2. Single Responsibility: Manages persistence."""
    def __init__(self) -> None:
        self._db: Dict[str, User] = {}

    def save(self, user: User) -> None:
        self._db[user.username] = user
        print(f"[UserRepository] User '{user.username}' persisted.")

    def get_by_username(self, username: str) -> User:
        return self._db[username]


class EmailService:
    """3. Single Responsibility: Handles external email communications."""
    def send_welcome_email(self, recipient_email: str, username: str) -> None:
        print(f"[EmailService] Welcome email sent to {recipient_email} for user '{username}'.")


class UserReportGenerator:
    """4. Single Responsibility: Generates user reports."""
    def generate_summary(self, user: User) -> str:
        return f"=== USER REPORT ===\nUsername: {user.username}\nEmail: {user.email}\nStatus: Active\n"


if __name__ == "__main__":
    # Orchestration of single-responsibility classes
    user = User(username="neo", email="neo@matrix.io")

    repo = UserRepository()
    repo.save(user)

    mailer = EmailService()
    mailer.send_welcome_email(user.email, user.username)

    reporter = UserReportGenerator()
    print("\n" + reporter.generate_summary(user))
