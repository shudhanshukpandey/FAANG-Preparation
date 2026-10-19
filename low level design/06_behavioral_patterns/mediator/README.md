# Mediator Pattern

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.


## Overview
- **Intent**: Define an object that encapsulates how a set of objects interact. Mediator promotes loose coupling by keeping objects from referring to each other explicitly, and it lets you vary their interaction independently.
- **Classification**: Behavioral Pattern.
- **Problem It Solves**: In a network of $N$ objects, direct communication requires $O(N^2)$ dependencies (chaotic mesh). A Mediator introduces a central hub, reducing complexity to $O(N)$ star topology.

## Architecture & Data Flow

```mermaid
graph TD
    subgraph ChaoticMesh [Anti-Pattern: O(N^2) Direct Mesh]
        PlaneA <--> PlaneB
        PlaneB <--> PlaneC
        PlaneC <--> PlaneA
        PlaneD <--> PlaneA
        PlaneD <--> PlaneB
    end

    subgraph StarMediator [Mediator: O(N) Star Topology]
        Plane1 --> ATC[Air Traffic Controller Mediator]
        Plane2 --> ATC
        Plane3 --> ATC
        ATC --> Plane1
        ATC --> Plane2
        ATC --> Plane3
    end
```

## FAANG Interview Significance
- Typical interview questions: Chatroom application (Slack/Discord channels), Air Traffic Controller, UI Form component coordination (checkbox disabling text inputs).
