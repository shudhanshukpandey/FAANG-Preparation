"""Bridge Pattern: Decoupling abstraction from implementation hierarchies."""

from abc import ABC, abstractmethod


# 1. Implementation Interface (Implementor)
class Device(ABC):
    @abstractmethod
    def is_enabled(self) -> bool:
        pass

    @abstractmethod
    def enable(self) -> None:
        pass

    @abstractmethod
    def disable(self) -> None:
        pass

    @abstractmethod
    def set_volume(self, percent: int) -> None:
        pass


# 2. Concrete Implementors
class SonyTV(Device):
    def __init__(self) -> None:
        self._on = False
        self._vol = 20

    def is_enabled(self) -> bool:
        return self._on

    def enable(self) -> None:
        self._on = True
        print("[SonyTV] Powered ON with Bravia XR Engine.")

    def disable(self) -> None:
        self._on = False
        print("[SonyTV] Standby mode.")

    def set_volume(self, percent: int) -> None:
        self._vol = max(0, min(100, percent))
        print(f"[SonyTV] Volume set to {self._vol}%")


class SmartRadio(Device):
    def __init__(self) -> None:
        self._on = False
        self._vol = 15

    def is_enabled(self) -> bool:
        return self._on

    def enable(self) -> None:
        self._on = True
        print("[Radio] FM Frequency tuner active.")

    def disable(self) -> None:
        self._on = False
        print("[Radio] Audio powered down.")

    def set_volume(self, percent: int) -> None:
        self._vol = max(0, min(100, percent))
        print(f"[Radio] Speaker volume: {self._vol}%")


# 3. Abstraction
class RemoteControl:
    def __init__(self, device: Device) -> None:
        # Bridge reference
        self.device = device

    def toggle_power(self) -> None:
        if self.device.is_enabled():
            self.device.disable()
        else:
            self.device.enable()

    def volume_up(self) -> None:
        self.device.set_volume(30)


# 4. Refined Abstraction
class AdvancedSmartRemote(RemoteControl):
    def mute(self) -> None:
        print("[AdvancedSmartRemote] One-touch Mute triggered.")
        self.device.set_volume(0)


if __name__ == "__main__":
    tv = SonyTV()
    radio = SmartRadio()

    basic_tv_remote = RemoteControl(tv)
    basic_tv_remote.toggle_power()
    basic_tv_remote.volume_up()

    print("-" * 40)
    advanced_radio_remote = AdvancedSmartRemote(radio)
    advanced_radio_remote.toggle_power()
    advanced_radio_remote.mute()
