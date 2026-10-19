"""Object Pool Pattern: Thread-safe connection pool with context manager support."""

import queue
import time
from typing import Optional


class PooledDatabaseConnection:
    def __init__(self, conn_id: int) -> None:
        self.conn_id = conn_id
        self.is_valid = True
        print(f"  [Pool Factory] Expensive socket connection #{self.conn_id} established.")

    def execute_query(self, sql: str) -> str:
        return f"Result of '{sql}' on Conn #{self.conn_id}"

    def reset(self) -> None:
        # Reset state before returning to pool
        pass


class ConnectionPool:
    def __init__(self, size: int = 2) -> None:
        self.size = size
        self._available: queue.Queue[PooledDatabaseConnection] = queue.Queue(maxsize=size)
        for i in range(1, size + 1):
            self._available.put(PooledDatabaseConnection(conn_id=i))

    def acquire(self, timeout_sec: float = 1.0) -> PooledDatabaseConnection:
        try:
            conn = self._available.get(timeout=timeout_sec)
            print(f"[Pool] Leased Connection #{conn.conn_id}. Available in pool: {self._available.qsize()}")
            return conn
        except queue.Empty:
            raise TimeoutError(f"Connection pool exhausted! Timed out waiting after {timeout_sec}s.")

    def release(self, conn: PooledDatabaseConnection) -> None:
        conn.reset()
        self._available.put(conn)
        print(f"[Pool] Returned Connection #{conn.conn_id}. Available in pool: {self._available.qsize()}")

    # Python context manager support
    def get_connection(self, timeout_sec: float = 1.0):
        class ConnectionContext:
            def __init__(self, pool: ConnectionPool):
                self.pool = pool
                self.conn: Optional[PooledDatabaseConnection] = None

            def __enter__(self) -> PooledDatabaseConnection:
                self.conn = self.pool.acquire(timeout_sec)
                return self.conn

            def __exit__(self, exc_type, exc_val, exc_tb) -> None:
                if self.conn:
                    self.pool.release(self.conn)

        return ConnectionContext(self)


if __name__ == "__main__":
    pool = ConnectionPool(size=2)

    print("\n--- 1. Using Context Manager to borrow and auto-return ---")
    with pool.get_connection() as conn:
        print("Query executed:", conn.execute_query("SELECT NOW();"))

    print("\n--- 2. Demonstrating Pool Exhaustion & Timeout ---")
    conn1 = pool.acquire()
    conn2 = pool.acquire()

    try:
        # Requesting a 3rd connection when capacity is 2
        print("Attempting to acquire 3rd connection (should time out)...")
        pool.acquire(timeout_sec=0.2)
    except TimeoutError as err:
        print("Expected timeout caught:", err)

    # Release back
    pool.release(conn1)
    pool.release(conn2)
