# Scalability: Horizontal vs Vertical Scaling

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

## Overview
Scalability is the property of a system to handle a growing amount of work by adding resources to the system.

### Vertical Scaling (Scale-Up)
- **Concept**: Adding more power (CPU, RAM, NVMe SSDs) to an existing server.
- **Pros**: Zero architectural complexity; no distributed coordination or network latency.
- **Cons**: Hard hardware ceiling; exponentially expensive; Single Point of Failure (SPOF).

### Horizontal Scaling (Scale-Out)
- **Concept**: Adding more nodes to the pool (e.g. EC2 instances, Kubernetes pods).
- **Pros**: Virtually unlimited ceiling; high fault tolerance; cost-effective commodity hardware.
- **Cons**: Requires stateless application tier; requires load balancers and distributed state management.

## Real-World Case Study
- **Netflix**: Runs tens of thousands of stateless Spring Boot / Node.js microservice instances behind AWS ALBs, dynamically auto-scaling based on regional prime-time streaming demands.
