# Domain-Driven Design (DDD): Aggregate Roots & Domain Events

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

## Overview
- **Intent**: Enforce transactional boundaries around complex domain model hierarchies via Aggregate Roots while cleanly broadcasting state changes through decoupled Domain Events.
- **Classification**: Enterprise Backend / Tactical DDD Pattern.
- **Real-World Parallels**: Order/Billing Aggregates in E-Commerce (Shopify, Amazon), Event Sourcing foundations.

## Core Features
1. **Aggregate Root**: The single entrypoint (`OrderAggregate`) that controls access and ensures invariant consistency for all child entities (`OrderLineItem`).
2. **Encapsulated State Mutation**: External code cannot mutate line items directly; all modifications pass through aggregate methods.
3. **Internal Event Recording**: Business events (e.g. `OrderPlacedEvent`, `OrderCancelledEvent`) are recorded inside the aggregate during state transitions.
4. **Post-Commit Dispatch**: Domain event publishers flush recorded events to message buses and notification handlers only after the database transaction succeeds.
