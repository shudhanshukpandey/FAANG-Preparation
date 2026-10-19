"""Content-Addressable Object Storage (S3-Style) Simulation."""
import hashlib

class S3ObjectStore:
    def __init__(self):
        self.metadata = {}
        self.blobs = {}
    def put_object(self, bucket: str, key: str, data: bytes) -> str:
        sha256 = hashlib.sha256(data).hexdigest()
        self.blobs[sha256] = data
        self.metadata[f"{bucket}/{key}"] = {"hash": sha256, "size": len(data)}
        return sha256
    def get_object(self, bucket: str, key: str) -> bytes:
        meta = self.metadata[f"{bucket}/{key}"]
        return self.blobs[meta["hash"]]

def run_tests():
    s3 = S3ObjectStore()
    payload = b"Video File Content"
    sha = s3.put_object("media", "vid1.mp4", payload)
    assert s3.get_object("media", "vid1.mp4") == payload
    print("✅ block_file_object_storage passed!")

if __name__ == "__main__":
    run_tests()
