"""Factory Method Pattern: Deferring object creation to specialized creator subclasses."""

from abc import ABC, abstractmethod


# 1. Product Interface
class Notification(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str) -> bool:
        pass


# 2. Concrete Products
class EmailNotification(Notification):
    def send(self, recipient: str, message: str) -> bool:
        print(f"[Email SMTP] Sent email to {recipient}: '{message}'")
        return True


class SMSNotification(Notification):
    def send(self, recipient: str, message: str) -> bool:
        print(f"[Twilio SMS Gateway] Sent SMS to {recipient}: '{message}'")
        return True


class PushNotification(Notification):
    def send(self, recipient: str, message: str) -> bool:
        print(f"[Firebase FCM] Dispatched push notification to device token {recipient}: '{message}'")
        return True


# 3. Creator (Declares the factory method)
class NotificationCreator(ABC):
    @abstractmethod
    def create_notification(self) -> Notification:
        """Factory Method to be overridden by subclasses."""
        pass

    def notify(self, recipient: str, message: str) -> bool:
        # Core business workflow uses the product returned by the factory method
        product = self.create_notification()
        return product.send(recipient, message)


# 4. Concrete Creators
class EmailNotificationCreator(NotificationCreator):
    def create_notification(self) -> Notification:
        return EmailNotification()


class SMSNotificationCreator(NotificationCreator):
    def create_notification(self) -> Notification:
        return SMSNotification()


class PushNotificationCreator(NotificationCreator):
    def create_notification(self) -> Notification:
        return PushNotification()


if __name__ == "__main__":
    # Client selects or is configured with a creator without hardcoding product instantiation
    creators = [EmailNotificationCreator(), SMSNotificationCreator(), PushNotificationCreator()]

    for creator in creators:
        creator.notify("user_alex", "Your security verification code is 492019")
