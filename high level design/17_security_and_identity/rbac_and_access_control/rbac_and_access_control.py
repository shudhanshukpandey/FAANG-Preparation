"""RBAC & ABAC Policy Engine Simulation."""
class AccessControlPolicy:
    def __init__(self):
        self.role_permissions = {
            "admin": {"read", "write", "delete"},
            "editor": {"read", "write"},
            "viewer": {"read"}
        }

    def check_access(self, role: str, action: str, owner_id: str, requester_id: str) -> bool:
        # Role check
        perms = self.role_permissions.get(role, set())
        if action not in perms:
            return False
        # Attribute check (e.g. only owner or admin can delete)
        if action == "delete" and role != "admin" and owner_id != requester_id:
            return False
        return True

def run_tests():
    ac = AccessControlPolicy()
    assert ac.check_access("editor", "write", "user1", "user1") is True
    assert ac.check_access("viewer", "write", "user1", "user1") is False
    assert ac.check_access("editor", "delete", "user1", "user2") is False
    assert ac.check_access("admin", "delete", "user1", "user2") is True
    print("✅ rbac_and_access_control passed!")

if __name__ == "__main__":
    run_tests()
