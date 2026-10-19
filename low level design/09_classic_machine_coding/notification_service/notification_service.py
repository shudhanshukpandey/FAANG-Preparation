"""Multi-Channel Notification Service: Factory, Strategy, and Preferences management."""

from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, List, Optional


class ChannelType(Enum):
    EMAIL = "EMAIL"
    SMS = "SMS"
    PUSH = "PUSH"


class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4  # OTPs, Security alerts


# 1. Channel Interface & Concrete Implementations
class NotificationChannel(ABC):
    @abstractmethod
    def deliver(self, recipient: str, title: str, body: str) -> bool:
        pass


class EmailChannel(NotificationChannel):
    def deliver(self, recipient: str, title: str, body: str) -> bool:
        print(f"  [SendGrid Email 📧 -> {recipient}] Subject: '{title}' | Body: '{body}'")
        return True


class SMSChannel(NotificationChannel):
    def deliver(self, recipient: str, title: str, body: str) -> bool:
        print(f"  [Twilio SMS 📱 -> {recipient}] '{title}: {body}'")
        return True


class PushChannel(NotificationChannel):
    def deliver(self, recipient: str, title: str, body: str) -> bool:
        print(f"  [Firebase FCM 🔔 -> {recipient}] Payload: '{title} - {body}'")
        return True


# 2. Channel Factory
class ChannelFactory:
    _channels: Dict[ChannelType, NotificationChannel] = {
        ChannelType.EMAIL: EmailChannel(),
        ChannelType.SMS: SMSChannel(),
        ChannelType.PUSH: PushChannel()
    }

    @classmethod
    def get_channel(cls, channel_type: ChannelType) -> NotificationChannel:
        if channel_type not in cls._channels:
            raise ValueError(f"Unsupported channel type: {channel_type}")
        return cls._channels[channel_type]


# 3. User Preferences Service
class UserPreferencesService:
    def __init__(self) -> None:
        # User -> Set of opted-in channels
        self._opted_in: Dict[str, set[ChannelType]] = {
            "usr_alice": {ChannelType.EMAIL, ChannelType.PUSH},  # Opted out of SMS!
            "usr_bob": {ChannelType.EMAIL, ChannelType.SMS, ChannelType.PUSH}
        }

    def is_channel_allowed(self, user_id: str, channel: ChannelType, priority: Priority) -> bool:
        # CRITICAL notifications bypass user opt-out (e.g. 2FA security OTPs)
        if priority == Priority.CRITICAL:
            return True
        return channel in self._opted_in.get(user_id, set())


# 4. Notification Hub Facade
class NotificationServiceFacade:
    def __init__(self, prefs: UserPreferencesService) -> None:
        self.prefs = prefs

    def send(
        self,
        user_id: str,
        recipient_target: str,
        channel_type: ChannelType,
        title: str,
        message: str,
        priority: Priority = Priority.MEDIUM
    ) -> bool:
        print(f"\n[NotificationService] Processing {channel_type.value} for {user_id} (Priority: {priority.name})...")

        # Step 1: Check user preferences
        if not self.prefs.is_channel_allowed(user_id, channel_type, priority):
            print(f"  [Preferences Blocked ⚠️] User '{user_id}' has opted out of {channel_type.value}. Delivery aborted.")
            return False

        # Step 2: Acquire channel via Factory
        channel = ChannelFactory.get_channel(channel_type)

        # Step 3: Deliver notification
        return channel.deliver(recipient_target, title, message)


if __name__ == "__main__":
    prefs = UserPreferencesService()
    service = NotificationServiceFacade(prefs)

    # 1. Normal Marketing SMS to Alice (Alice opted out of SMS -> blocked!)
    service.send(
        user_id="usr_alice",
        recipient_target="+1-555-0199",
        channel_type=ChannelType.SMS,
        title="Spring Sale",
        message="50% off all courses today!",
        priority=Priority.LOW
    )

    # 2. Critical Security OTP SMS to Alice (Bypasses opt-out due to CRITICAL priority)
    service.send(
        user_id="usr_alice",
        recipient_target="+1-555-0199",
        channel_type=ChannelType.SMS,
        title="Security Alert",
        message="Your verification code is 884192. Do not share.",
        priority=Priority.CRITICAL
    )

    # 3. Push notification to Bob
    service.send(
        user_id="usr_bob",
        recipient_target="device_token_bob_iphone",
        channel_type=ChannelType.PUSH,
        title="Order Shipped",
        message="Your package is out for delivery today!"
    )
