# Block vs File vs Object Storage

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

- **Block Storage (EBS, SAN)**: Raw block volume for OS and high-IOPS databases.
- **File Storage (NFS, EFS)**: Hierarchical POSIX directory trees for shared access.
- **Object Storage (S3, GCS)**: Flat address space using HTTP REST APIs; infinite scalability, content-addressable blobs.
