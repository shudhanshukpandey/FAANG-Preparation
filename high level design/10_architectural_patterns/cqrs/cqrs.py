"""CQRS Simulation."""
class CQRSStore:
    def __init__(self):
        self.write_db = {}
        self.read_cache = {}
    def execute_command(self, user_id: str, name: str):
        self.write_db[user_id] = name
        # Project into read model
        self.read_cache[user_id] = {"id": user_id, "name": name, "view_count": 0}
    def execute_query(self, user_id: str):
        return self.read_cache.get(user_id)

def run_tests():
    cqrs = CQRSStore()
    cqrs.execute_command("u1", "Alice")
    assert cqrs.execute_query("u1")["name"] == "Alice"
    print("✅ cqrs passed!")

if __name__ == "__main__":
    run_tests()
