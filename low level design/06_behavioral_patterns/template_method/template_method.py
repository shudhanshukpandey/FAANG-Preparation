"""Template Method Pattern: Defining algorithm skeleton with deferred subclass steps."""

from abc import ABC, abstractmethod
from typing import Any, List


class DataETLPipeline(ABC):
    """Abstract base defining the invariant algorithm workflow."""

    # The Template Method: Final invariant skeleton
    def run_pipeline(self, source_path: str) -> List[dict]:
        print(f"\n=== Starting ETL Pipeline for: {source_path} ===")
        raw_data = self.extract(source_path)
        parsed_records = self.transform(raw_data)
        cleaned_records = self.clean_records(parsed_records)

        # Optional Hook
        if self.should_audit():
            self.audit_log(len(cleaned_records))

        self.load(cleaned_records)
        print("=== Pipeline Finished Successfully ===")
        return cleaned_records

    # Mandatory steps to be implemented by format-specific subclasses
    @abstractmethod
    def extract(self, source_path: str) -> str:
        pass

    @abstractmethod
    def transform(self, raw_data: str) -> List[dict]:
        pass

    # Common step shared across all pipelines
    def clean_records(self, records: List[dict]) -> List[dict]:
        print(f"[Base Pipeline] Sanitizing whitespace and null entries for {len(records)} records.")
        return [r for r in records if r]

    def load(self, records: List[dict]) -> None:
        print(f"[Base Pipeline] Loaded {len(records)} records into Data Warehouse.")

    # Hook with default behavior
    def should_audit(self) -> bool:
        return True

    def audit_log(self, record_count: int) -> None:
        print(f"[Audit Hook] Metric emitted: {record_count} items ingested.")


# Subclass 1: CSV Implementation
class CSVDataPipeline(DataETLPipeline):
    def extract(self, source_path: str) -> str:
        print(f"[CSV Extractor] Reading CSV bytes from {source_path}")
        return "id,name,score\n1,Alice,95\n2,Bob,88"

    def transform(self, raw_data: str) -> List[dict]:
        print("[CSV Transformer] Parsing comma-separated lines into dicts.")
        return [{"id": "1", "name": "Alice", "score": 95}, {"id": "2", "name": "Bob", "score": 88}]


# Subclass 2: JSON Implementation
class JSONDataPipeline(DataETLPipeline):
    def extract(self, source_path: str) -> str:
        print(f"[JSON Extractor] Fetching raw JSON from {source_path}")
        return '[{"id": "10", "name": "Charlie"}]'

    def transform(self, raw_data: str) -> List[dict]:
        print("[JSON Transformer] Deserializing JSON string.")
        return [{"id": "10", "name": "Charlie"}]


if __name__ == "__main__":
    csv_pipeline = CSVDataPipeline()
    csv_pipeline.run_pipeline("s3://bucket/reports/q3.csv")

    json_pipeline = JSONDataPipeline()
    json_pipeline.run_pipeline("https://api.partner.io/v2/stream.json")
