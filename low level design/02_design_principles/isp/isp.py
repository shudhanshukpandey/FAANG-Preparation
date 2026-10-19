"""Interface Segregation Principle (ISP): Splitting fat interfaces into focused role interfaces."""

from abc import ABC, abstractmethod


# -------------------------------------------------------------
# Anti-Pattern: Fat Interface forcing useless implementations
# -------------------------------------------------------------
class IMultiFunctionDeviceViolating(ABC):
    @abstractmethod
    def print_document(self, content: str) -> None:
        pass

    @abstractmethod
    def scan_document(self) -> str:
        pass

    @abstractmethod
    def fax_document(self, phone: str, content: str) -> None:
        pass


class BasicPrinterViolating(IMultiFunctionDeviceViolating):
    def print_document(self, content: str) -> None:
        print(f"Printing: {content}")

    # Forced to implement methods it cannot physically perform!
    def scan_document(self) -> str:
        raise NotImplementedError("Basic printer cannot scan!")

    def fax_document(self, phone: str, content: str) -> None:
        raise NotImplementedError("Basic printer cannot fax!")


# -------------------------------------------------------------
# Clean Refactor: Granular Role Interfaces
# -------------------------------------------------------------
class Printer(ABC):
    @abstractmethod
    def print_document(self, content: str) -> None:
        pass


class Scanner(ABC):
    @abstractmethod
    def scan_document(self) -> str:
        pass


class Fax(ABC):
    @abstractmethod
    def fax_document(self, phone: str, content: str) -> None:
        pass


# 1. Single-purpose class only implements what it uses
class StandardPrinter(Printer):
    def print_document(self, content: str) -> None:
        print(f"[StandardPrinter] Printing: {content}")


# 2. Multi-function class composes multiple interfaces cleanly
class EnterpriseOfficeHub(Printer, Scanner, Fax):
    def print_document(self, content: str) -> None:
        print(f"[OfficeHub] High-speed laser printing: {content}")

    def scan_document(self) -> str:
        return "[OfficeHub] High-resolution optical scan complete."

    def fax_document(self, phone: str, content: str) -> None:
        print(f"[OfficeHub] Fax transmitted to {phone}")


if __name__ == "__main__":
    printer = StandardPrinter()
    printer.print_document("Q3 Financial Report")

    hub = EnterpriseOfficeHub()
    hub.print_document("Memo")
    print(hub.scan_document())
    hub.fax_document("+1-800-555-0199", "Signed Contract")
