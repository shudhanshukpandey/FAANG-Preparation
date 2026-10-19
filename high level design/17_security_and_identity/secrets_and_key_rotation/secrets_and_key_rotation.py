"""Secrets Lease & Automated Key Rotation Simulation."""
class KeyManager:
    def __init__(self):
        self.keys = {1: "key_v1_secret"}
        self.active_version = 1

    def rotate_key(self, new_key: str):
        self.active_version += 1
        self.keys[self.active_version] = new_key

    def decrypt(self, version: int, ciphertext: str) -> str:
        # Decrypt using versioned key
        key = self.keys[version]
        return f"decrypted_with_{key}"

def run_tests():
    km = KeyManager()
    assert km.active_version == 1
    km.rotate_key("key_v2_secret")
    assert km.active_version == 2
    # Old ciphertext can still be decrypted with key v1
    assert "key_v1_secret" in km.decrypt(1, "data")
    print("✅ secrets_and_key_rotation passed!")

if __name__ == "__main__":
    run_tests()
