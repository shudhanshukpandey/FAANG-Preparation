"""TLS 1.3 Symmetric Key Derivation & AES Envelope Encryption Simulation."""
import hashlib
import hmac

class EncryptionPipeline:
    def derive_session_key(self, client_share: bytes, server_share: bytes) -> bytes:
        # ECDHE key exchange simulation
        return hashlib.sha256(client_share + server_share).digest()

    def encrypt_envelope(self, data: bytes, kek: bytes) -> tuple[bytes, bytes]:
        # KEK: Key Encryption Key, DEK: Data Encryption Key
        dek = hashlib.sha256(b"random_dek").digest()
        encrypted_dek = hmac.new(kek, dek, hashlib.sha256).digest()
        # Simulated payload encryption
        cipher = bytes(b ^ 0xAA for b in data)
        return cipher, encrypted_dek

def run_tests():
    ep = EncryptionPipeline()
    k1 = ep.derive_session_key(b"client_pub", b"server_pub")
    assert len(k1) == 32
    cipher, enc_dek = ep.encrypt_envelope(b"secret_data", kek=b"master_kek")
    assert cipher != b"secret_data"
    print("✅ tls_and_encryption passed!")

if __name__ == "__main__":
    run_tests()
