"""Distributed Lock Manager with Fencing Tokens Simulation."""
import time

class DistributedLockManager:
    def __init__(self):
        self.lock_owner = None
        self.lock_expiry = 0
        self.fencing_counter = 0

    def acquire(self, client_id: str, ttl_ms: int = 1000) -> tuple[bool, int]:
        now = int(time.time() * 1000)
        if self.lock_owner is None or now > self.lock_expiry:
            self.lock_owner = client_id
            self.lock_expiry = now + ttl_ms
            self.fencing_counter += 1
            return True, self.fencing_counter
        return False, 0

    def release(self, client_id: str):
        if self.lock_owner == client_id:
            self.lock_owner = None

def run_tests():
    dlm = DistributedLockManager()
    ok1, token1 = dlm.acquire("worker_1", 500)
    assert ok1 is True and token1 == 1
    ok2, _ = dlm.acquire("worker_2", 500)
    assert ok2 is False # Blocked
    dlm.release("worker_1")
    ok3, token2 = dlm.acquire("worker_2", 500)
    assert ok3 is True and token2 == 2 # Monotonically increasing fencing token
    print("✅ distributed_locks passed!")

if __name__ == "__main__":
    run_tests()
