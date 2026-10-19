"""Mediator Pattern: Centralized communication hub for chat participants."""

from abc import ABC, abstractmethod
from typing import Dict, List


# 1. Mediator Interface
class ChatMediator(ABC):
    @abstractmethod
    def send_message(self, message: str, sender: "User") -> None:
        pass

    @abstractmethod
    def add_user(self, user: "User") -> None:
        pass


# 2. Colleague
class User:
    def __init__(self, name: str, mediator: ChatMediator) -> None:
        self.name = name
        self.mediator = mediator
        self.mediator.add_user(self)

    def send(self, message: str) -> None:
        print(f"\n[{self.name} -> Chatroom]: '{message}'")
        self.mediator.send_message(message, sender=self)

    def receive(self, message: str, sender_name: str) -> None:
        print(f"  [{self.name}'s Screen] {sender_name}: '{message}'")


# 3. Concrete Mediator
class ChatRoomMediator(ChatMediator):
    def __init__(self, room_name: str) -> None:
        self.room_name = room_name
        self._users: List[User] = []

    def add_user(self, user: User) -> None:
        self._users.append(user)

    def send_message(self, message: str, sender: User) -> None:
        # Broadcast message to all colleagues except the sender
        for recipient in self._users:
            if recipient != sender:
                recipient.receive(message, sender_name=sender.name)


if __name__ == "__main__":
    dev_channel = ChatRoomMediator("general-engineering")

    alice = User("Alice", dev_channel)
    bob = User("Bob", dev_channel)
    charlie = User("Charlie", dev_channel)

    alice.send("Hey team, deployment is scheduled for 5 PM UTC.")
    bob.send("Acknowledged! DB migrations are ready.")
