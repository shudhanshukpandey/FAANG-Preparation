"""Abstract Factory Pattern: Producing families of related cloud compute and storage products."""

from abc import ABC, abstractmethod


# 1. Family Products: Compute and Storage
class ComputeInstance(ABC):
    @abstractmethod
    def launch(self) -> None:
        pass


class StorageBucket(ABC):
    @abstractmethod
    def store_file(self, filename: str) -> None:
        pass


# 2. AWS Concrete Product Implementations
class EC2Instance(ComputeInstance):
    def launch(self) -> None:
        print("[AWS] Launched EC2 t3.xlarge instance.")


class S3Bucket(StorageBucket):
    def store_file(self, filename: str) -> None:
        print(f"[AWS] Stored '{filename}' in S3 standard bucket.")


# 3. GCP Concrete Product Implementations
class GCEInstance(ComputeInstance):
    def launch(self) -> None:
        print("[GCP] Launched Google Compute Engine e2-standard-4 instance.")


class GCSBucket(StorageBucket):
    def store_file(self, filename: str) -> None:
        print(f"[GCP] Stored '{filename}' in Google Cloud Storage multi-regional bucket.")


# 4. Abstract Factory Interface
class CloudResourceFactory(ABC):
    @abstractmethod
    def create_compute(self) -> ComputeInstance:
        pass

    @abstractmethod
    def create_storage(self) -> StorageBucket:
        pass


# 5. Concrete Cloud Factories
class AWSResourceFactory(CloudResourceFactory):
    def create_compute(self) -> ComputeInstance:
        return EC2Instance()

    def create_storage(self) -> StorageBucket:
        return S3Bucket()


class GCPResourceFactory(CloudResourceFactory):
    def create_compute(self) -> ComputeInstance:
        return GCEInstance()

    def create_storage(self) -> StorageBucket:
        return GCSBucket()


# Client code interacts only with the abstract factory
def deploy_infrastructure(factory: CloudResourceFactory) -> None:
    server = factory.create_compute()
    storage = factory.create_storage()

    server.launch()
    storage.store_file("deployment_manifest.yaml")


if __name__ == "__main__":
    print("--- Deploying on AWS ---")
    deploy_infrastructure(AWSResourceFactory())

    print("\n--- Deploying on GCP ---")
    deploy_infrastructure(GCPResourceFactory())
