"""Concurrency & Locking: Demonstrating Pessimistic (Mutex) vs Optimistic (Versioning) locking."""

import threading
import time
from typing import Optional


# -------------------------------------------------------------
# 1. Pessimistic Locking Implementation (Mutex / SELECT FOR UPDATE)
# -------------------------------------------------------------
class PessimisticInventory:
    def __init__(self, stock: int) -> None:
        self.stock = stock
        self._lock = threading.Lock()

    def reserve_item(self, user_id: str) -> bool:
        # Blocks all other threads until the lock is released
        with self._lock:
            if self.stock > 0:
                time.sleep(0.01)  # Simulate network / DB write latency
                self.stock -= 1
                print(f"[Pessimistic ✅] Seat booked for {user_id}. Remaining: {self.stock}")
                return True
            print(f"[Pessimistic ❌] Sold out! Booking denied for {user_id}.")
            return False


# -------------------------------------------------------------
# 2. Optimistic Locking Implementation (Version Checking / CAS)
# -------------------------------------------------------------
class OptimisticProduct:
    def __init__(self, stock: int) -> None:
        self.stock = stock
        self.version = 1
        self._internal_lock = threading.Lock()  # Simulates DB engine CAS atomic update

    def get_snapshot(self) -> tuple[int, int]:
        """Simulates non-blocking dirty read: (stock, version)."""
        return (self.stock, self.version)

    def compare_and_swap_purchase(self, expected_version: int, user_id: str) -> bool:
        """Simulates: UPDATE product SET stock=stock-1, version=version+1 WHERE version=:expected_version"""
        with self._internal_lock:
            if self.version != expected_version:
                print(f"[Optimistic ⚠️ Conflict] Stale version for {user_id} (expected v{expected_version}, DB has v{self.version})")
                return False

            if self.stock <= 0:
                print(f"[Optimistic ❌ Sold Out] Out of stock for {user_id}.")
                return False

            self.stock -= 1
            self.version += 1
            print(f"[Optimistic ✅] Purchased for {user_id}! DB updated to version {self.version}.")
            return True


def simulate_optimistic_client(product: OptimisticProduct, user_id: str) -> None:
    # 1. Read current version
    stock, version = product.get_snapshot()
    time.sleep(0.01)  # Simulate user thinking / typing credit card details
    # 2. Attempt commit with observed version
    success = product.compare_and_swap_purchase(version, user_id)


if __name__ == "__main__":
    print("--- 1. Testing Pessimistic Locking with Concurrent Threads ---")
    pessimistic_inv = PessimisticInventory(stock=1)  # Only 1 ticket left!
    threads = [
        threading.Thread(target=pessimistic_inv.reserve_item, args=(f"User_{i}",))
        for i in range(1, 4)
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print("\n--- 2. Testing Optimistic Locking under Simultaneous Contention ---")
    opt_product = OptimisticProduct(stock=1)  # Only 1 ticket left!
    opt_threads = [
        threading.Thread(target=simulate_optimistic_client, args=(opt_product, f"Buyer_{i}"))
        for i in range(1, 4)
    ]
    for t in opt_threads:
        t.start()
    for t in opt_threads:
        t.join()
