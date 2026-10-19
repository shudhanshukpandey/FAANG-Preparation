"""SQL vs NoSQL Simulation."""
class SQLStore:
    def __init__(self):
        self.users = {"u1": {"id": "u1", "name": "Alice"}}
        self.orders = {"o1": {"id": "o1", "user_id": "u1", "item": "Book"}}
    def join_user_order(self, order_id: str) -> dict:
        o = self.orders[order_id]
        u = self.users[o["user_id"]]
        return {"order_id": o["id"], "customer": u["name"], "item": o["item"]}

class NoSQLDocStore:
    def __init__(self):
        # Denormalized single document
        self.docs = {"o1": {"id": "o1", "customer_name": "Alice", "item": "Book"}}
    def get_order(self, order_id: str) -> dict:
        return self.docs[order_id]

def run_tests():
    sql = SQLStore()
    assert sql.join_user_order("o1") == {"order_id": "o1", "customer": "Alice", "item": "Book"}
    nosql = NoSQLDocStore()
    assert nosql.get_order("o1") == {"id": "o1", "customer_name": "Alice", "item": "Book"}
    print("✅ sql_vs_nosql passed!")

if __name__ == "__main__":
    run_tests()
