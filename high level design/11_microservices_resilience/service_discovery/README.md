# Service Discovery & Heartbeat Registries

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

- **Dynamic IP Topology**: Containers and pods spin up and down with ephemeral IP addresses.
- **Service Registry (Consul, Eureka, ZooKeeper)**: Nodes register on boot and renew leases via heartbeats.
