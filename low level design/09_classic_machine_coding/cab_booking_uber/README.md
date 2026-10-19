# Ride-Sharing & Cab Booking System (Mini-Uber)

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

## Overview
- **Intent**: Coordinate riders and drivers in a spatial grid, calculating proximity, applying dynamic surge multipliers, and driving trips through a strict state machine.
- **Classification**: Classic Machine Coding / Real-Time Dispatch.
- **Real-World Parallels**: Uber, Lyft, Grab, Ola.

## Core Features
1. **Driver & Rider Spatial Tracking**: Geolocation distance estimation for pickup ETA and trip routing.
2. **Proximity Matching**: Filters available drivers within a search radius (e.g. Euclidean or Geohash-bounded) to find the optimal match.
3. **Dynamic Surge Pricing**: Computes surge multipliers based on real-time `Demand / Available Drivers` ratio.
4. **Trip State Machine**: Enforces valid transitions (`REQUESTED` -> `ACCEPTED` -> `IN_PROGRESS` -> `COMPLETED` / `CANCELLED`).
