"""Polymorphism: Runtime method overriding and functional single-dispatch."""

from abc import ABC, abstractmethod
from functools import singledispatch
from typing import List


# 1. Runtime Dynamic Polymorphism (Subtype Polymorphism)
class NotificationChannel(ABC):
    @abstractmethod
    def send(self, recipient: str, body: str) -> bool:
        pass


class EmailChannel(NotificationChannel):
    def send(self, recipient: str, body: str) -> bool:
        print(f"[Email -> {recipient}]: Sending SMTP payload: '{body}'")
        return True


class SMSChannel(NotificationChannel):
    def send(self, recipient: str, body: str) -> bool:
        print(f"[SMS -> {recipient}]: Dispatching via Twilio SMS: '{body}'")
        return True


class PushChannel(NotificationChannel):
    def send(self, recipient: str, body: str) -> bool:
        print(f"[Push -> {recipient}]: Dispatching to Firebase FCM: '{body}'")
        return True


def broadcast_alert(channels: List[NotificationChannel], user: str, message: str) -> None:
    # Polymorphic call: Client code does not care which concrete channel it is invoking!
    for channel in channels:
        channel.send(user, message)


# 2. Compile/Dispatch-time Polymorphism via @singledispatch
@singledispatch
def format_data(payload) -> str:
    raise NotImplementedError(f"Unsupported payload type: {type(payload)}")


@format_data.register(str)
def _(payload: str) -> str:
    return f"String: '{payload.strip().upper()}'"


@format_data.register(int)
def _(payload: int) -> str:
    return f"Integer: {payload:,} (Hex: {hex(payload)})"


@format_data.register(list)
def _(payload: list) -> str:
    return f"List with {len(payload)} items: {', '.join(map(str, payload))}"


if __name__ == "__main__":
    print("--- Dynamic Subtype Polymorphism ---")
    active_channels: List[NotificationChannel] = [EmailChannel(), SMSChannel(), PushChannel()]
    broadcast_alert(active_channels, "dev@example.com", "System CPU usage exceeded 90%")

    print("\n--- Static Single-Dispatch Polymorphism ---")
    print(format_data("   urgent alert   "))
    print(format_data(1000000))
    print(format_data(["alpha", "beta", "gamma"]))
