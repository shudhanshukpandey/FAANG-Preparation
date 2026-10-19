# Single Responsibility Principle (SRP)

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.


## Overview
- **Definition**: "A class should have one, and only one, reason to change."
- **God Class (Anti-Pattern)**: A single class that mixes business logic, database persistence, email notification, and report generation.
- **Signs of SRP Violation**:
  - Too many imports from completely different domains (e.g., `smtplib`, `sqlite3`, `reportlab`).
  - Merge conflicts where multiple developers edit the same file for different reasons.

## Architecture & Data Flow

```mermaid
graph TD
    subgraph AntiPattern [God Class: 4 Reasons to Change]
        UserGod[UserGodClass]
        UserGod -->|Reason 1| Auth[User Profile Logic]
        UserGod -->|Reason 2| DB[SQL DB Queries]
        UserGod -->|Reason 3| SMTP[Sending Welcome Email]
        UserGod -->|Reason 4| PDF[Exporting PDF Statements]
    end

    subgraph RefactoredSRP [SRP Compliant: 1 Reason to Change Each]
        User[User Model]
        UserRepo[UserRepository]
        EmailService[EmailNotificationService]
        StatementGen[StatementGenerator]

        User --> UserRepo
        User --> EmailService
        User --> StatementGen
    end
```

## FAANG Interview Significance
- The foundation of 3-tier / Clean Architecture in FastAPI, Flask, and Django.
- Enables parallel development and isolated unit testing.
