# Consistent Hashing with Virtual Nodes

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

## The Problem with Modulo Hashing
Traditional sharding uses:
$$\text{server} = \text{hash}(key) \pmod N$$
When $N$ changes (adding or removing a server), **almost $100\%$ of keys are remapped**, causing massive cache stampedes and database meltdowns.

## Consistent Hashing Mechanics
1. **The Hash Ring**: Map both server IDs and data keys to a circular $2^{128}$ integer space.
2. **Clockwise Lookup**: A key is assigned to the first server whose hash value is $\ge$ the key's hash.
3. **Virtual Nodes**: Each physical server is assigned $K$ virtual points on the ring (e.g. $K = 100$), guaranteeing uniform balance and preventing non-uniform hash clusters.
4. **Minimal Resharding**: When adding/removing 1 node from $N$, only $\frac{1}{N}$ of the total keys migrate.
