"""Database Connection Pooling Simulation."""
class ConnectionPool:
    def __init__(self, size=2):
        self.available = [f"conn_{i}" for i in range(size)]
    def acquire(self):
        return self.available.pop(0) if self.available else None
    def release(self, conn):
        self.available.append(conn)

def run_tests():
    pool = ConnectionPool(2)
    c1 = pool.acquire()
    c2 = pool.acquire()
    assert pool.acquire() is None # Pool exhausted
    pool.release(c1)
    assert pool.acquire() == "conn_0"
    print("✅ connection_pooling passed!")

if __name__ == "__main__":
    run_tests()
