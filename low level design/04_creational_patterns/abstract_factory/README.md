# Abstract Factory Pattern

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.


## Overview
- **Intent**: Provide an interface for creating **families of related or dependent objects** without specifying their concrete classes.
- **Difference from Factory Method**:
  - *Factory Method* creates **one product** using inheritance.
  - *Abstract Factory* creates a **family of related products** using object composition.

## Architecture & Data Flow

```mermaid
classDiagram
    class CloudResourceFactory {
        <<interface>>
        +create_compute()* ComputeInstance
        +create_storage()* StorageBucket
    }

    class AWSResourceFactory {
        +create_compute() ComputeInstance
        +create_storage() StorageBucket
    }

    class GCPResourceFactory {
        +create_compute() ComputeInstance
        +create_storage() StorageBucket
    }

    class ComputeInstance {
        <<interface>>
        +launch()
    }
    class StorageBucket {
        <<interface>>
        +store(data: str)
    }

    CloudResourceFactory <|.. AWSResourceFactory
    CloudResourceFactory <|.. GCPResourceFactory
    AWSResourceFactory ..> EC2Instance : creates
    AWSResourceFactory ..> S3Bucket : creates
    GCPResourceFactory ..> GCEInstance : creates
    GCPResourceFactory ..> GCSBucket : creates
```

## FAANG Interview Significance
- Typical interview questions: Cross-platform UI toolkit (Mac vs Windows Buttons, Checkboxes, Dialogs), Multi-cloud infrastructure provisioners (AWS vs GCP vs Azure), Database connectors (SQL vs NoSQL query generators).
