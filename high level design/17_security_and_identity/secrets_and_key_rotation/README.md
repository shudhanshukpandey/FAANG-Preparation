# Secrets Management & Key Rotation

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

- **Dynamic Secrets (HashiCorp Vault, AWS KMS)**: Ephemeral database credentials generated on demand with TTL expiration.
- **Key Versioning**: Key rotation without immediate table re-encryption; decrypts historical rows using versioned metadata.
