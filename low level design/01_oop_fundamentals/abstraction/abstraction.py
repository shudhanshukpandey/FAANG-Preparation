"""Abstraction: Exposing high-level contracts while hiding complex implementation details."""

from abc import ABC, abstractmethod
import time


class CloudStorageClient(ABC):
    """Abstract interface defining the contract for any cloud storage provider."""

    @abstractmethod
    def upload_file(self, file_path: str, destination_name: str) -> str:
        """Uploads file and returns the public/signed URL."""
        pass

    @abstractmethod
    def delete_file(self, destination_name: str) -> bool:
        """Deletes file by key."""
        pass


class S3CloudStorageClient(CloudStorageClient):
    """Concrete implementation hiding complex AWS S3 signing, chunking, and HTTP retry logic."""

    def __init__(self, bucket: str, region: str) -> None:
        self.bucket = bucket
        self.region = region

    def _sign_request_v4(self, payload: bytes) -> str:
        # Complex internal crypto logic hidden from caller
        return f"AWS4-HMAC-SHA256-SIGNATURE-{hash(payload)}"

    def _retry_with_exponential_backoff(self, payload: bytes) -> bool:
        # Complex networking resiliency hidden from caller
        time.sleep(0.01)
        return True

    def upload_file(self, file_path: str, destination_name: str) -> str:
        data = f"binary_data_from_{file_path}".encode("utf-8")
        signature = self._sign_request_v4(data)
        self._retry_with_exponential_backoff(data)

        url = f"https://{self.bucket}.s3.{self.region}.amazonaws.com/{destination_name}?sig={signature[:12]}"
        return url

    def delete_file(self, destination_name: str) -> bool:
        return True


if __name__ == "__main__":
    # The client interacts solely with the abstract representation
    storage: CloudStorageClient = S3CloudStorageClient(bucket="user-avatars-prod", region="us-east-1")
    file_url = storage.upload_file("avatar.png", "users/42/avatar.png")
    print(f"File successfully uploaded: {file_url}")
