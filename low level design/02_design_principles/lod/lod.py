"""Law of Demeter (LoD): Avoiding train-wreck method chains via delegation."""


class Wallet:
    def __init__(self, balance: float) -> None:
        self.balance = balance

    def deduct(self, amount: float) -> bool:
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False


class Customer:
    def __init__(self, name: str, wallet: Wallet) -> None:
        self.name = name
        self._wallet = wallet  # Private to Customer

    # LoD Compliance: Customer delegates payment to its own wallet
    def pay(self, amount: float) -> bool:
        return self._wallet.deduct(amount)

    # Violating getter for anti-pattern demonstration
    def get_wallet(self) -> Wallet:
        return self._wallet


class Order:
    def __init__(self, order_id: str, customer: Customer, total_amount: float) -> None:
        self.order_id = order_id
        self.customer = customer
        self.total_amount = total_amount

    # LoD Compliance: Order speaks directly only to its immediate friend (customer)
    def complete_payment(self) -> bool:
        return self.customer.pay(self.total_amount)


# -------------------------------------------------------------
# Anti-Pattern vs Clean Comparison
# -------------------------------------------------------------
if __name__ == "__main__":
    wallet = Wallet(500.0)
    customer = Customer("Alice", wallet)
    order = Order("ORD-101", customer, 150.0)

    # 1. Anti-Pattern: Train wreck breaking encapsulation
    # print(order.customer.get_wallet().deduct(150.0))  # Strangers interacting!

    # 2. Clean Demeter compliant: Tell, Don't Ask
    success = order.complete_payment()
    print(f"Order #{order.order_id} completed successfully? {success}")
    print(f"Remaining customer balance: ${wallet.balance:.2f}")
