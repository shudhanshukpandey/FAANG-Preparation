"""Stateless JWT Token Simulation."""
import hmac, hashlib, base64, json

class JWTAuth:
    def __init__(self, secret: str):
        self.secret = secret.encode("utf-8")
    def create_token(self, payload: dict) -> str:
        body = base64.b64encode(json.dumps(payload).encode("utf-8")).decode("utf-8")
        sig = hmac.new(self.secret, body.encode("utf-8"), hashlib.sha256).hexdigest()
        return f"{body}.{sig}"
    def verify_token(self, token: str) -> dict:
        body, sig = token.split(".")
        expected = hmac.new(self.secret, body.encode("utf-8"), hashlib.sha256).hexdigest()
        if not hmac.compare_digest(sig, expected):
            raise PermissionError("Tampered token")
        return json.loads(base64.b64decode(body.encode("utf-8")).decode("utf-8"))

def run_tests():
    auth = JWTAuth("my_super_secret")
    tok = auth.create_token({"user": "Alice", "role": "admin"})
    decoded = auth.verify_token(tok)
    assert decoded["user"] == "Alice"
    print("✅ auth_and_tokens passed!")

if __name__ == "__main__":
    run_tests()
