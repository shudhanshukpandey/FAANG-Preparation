# TLS 1.3 & Envelope Encryption

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

- **TLS 1.3 (1-RTT Handshake)**: Eliminates insecure legacy ciphers, combining Diffie-Hellman key share in the Client Hello.
- **Envelope Encryption**: Data encrypted with local Data Encryption Key (DEK); DEK encrypted with Master Key (KEK) via KMS/Vault.
