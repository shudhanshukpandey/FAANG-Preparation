# DNS Resolution & Anycast Routing

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

- **DNS Hierarchy**: Browser Cache -> Recursive Resolver -> Root -> TLD -> Authoritative Nameserver.
- **Anycast**: Multiple servers across global locations advertise the same IP via BGP routing.
