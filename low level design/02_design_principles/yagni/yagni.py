"""YAGNI Principle: Implementing only what is immediately required."""

from dataclasses import dataclass
from typing import Optional


# -------------------------------------------------------------
# Anti-Pattern: Speculative Generalization
# -------------------------------------------------------------
@dataclass
class UserAccountSpeculative:
    email: str
    username: str
    password_hash: str
    # Unneeded speculative features for an internal MVP:
    web3_wallet_address: Optional[str] = None
    biometric_face_vector: Optional[list] = None
    metaverse_3d_avatar_mesh_url: Optional[str] = None
    quantum_encryption_seed: Optional[str] = None

    def sync_to_blockchain(self):
        # Thousands of lines of unmaintained speculative code
        pass


# -------------------------------------------------------------
# Clean Refactor: YAGNI
# -------------------------------------------------------------
@dataclass
class UserAccount:
    email: str
    username: str
    password_hash: str
    is_active: bool = True


if __name__ == "__main__":
    user = UserAccount(email="alice@tech.io", username="alice", password_hash="hash_abc123")
    print(f"Created lean, requirement-focused user model: {user}")
