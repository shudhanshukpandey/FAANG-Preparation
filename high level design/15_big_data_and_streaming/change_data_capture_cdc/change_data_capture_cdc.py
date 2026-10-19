"""Change Data Capture (CDC) via Outbox Simulation."""
class OutboxCDC:
    def __init__(self):
        self.wal_log = []
        self.subscribers = []
    def commit_transaction(self, table: str, op: str, row: dict):
        event = {"table": table, "op": op, "data": row}
        self.wal_log.append(event)
        self._notify(event)
    def _notify(self, event):
        for s in self.subscribers:
            s(event)

def run_tests():
    cdc = OutboxCDC()
    stream = []
    cdc.subscribers.append(lambda e: stream.append(e))
    cdc.commit_transaction("users", "INSERT", {"id": 1, "name": "Alice"})
    assert len(stream) == 1
    assert stream[0]["op"] == "INSERT"
    print("✅ change_data_capture_cdc passed!")

if __name__ == "__main__":
    run_tests()
