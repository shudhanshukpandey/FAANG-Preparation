# SOLID Principles Summary & Interview Cheat Sheet

## The 5 Pillars at a Glance

| Principle | Meaning | Violation Symptom | Clean Remedy |
| :--- | :--- | :--- | :--- |
| **S - Single Responsibility** | A class should have one, and only one, reason to change. | "God class", mixed concerns (DB + Email + Business Logic). | Split into cohesive collaborators (Domain Model, Repository, Service, Notifier). |
| **O - Open/Closed** | Open for extension, closed for modification. | Massive `if/elif/else` or `match` blocks when adding a new type. | Polymorphism, Strategy pattern, Abstract base classes. |
| **L - Liskov Substitution** | Subtypes must be substitutable for their supertypes. | Subclasses throwing `NotImplementedError` or changing invariants. | Re-evaluate inheritance tree; favor Composition over Inheritance. |
| **I - Interface Segregation** | Clients shouldn't depend on interfaces they don't use. | "Fat interface" with empty dummy stubs in simple subclasses. | Split into small, focused role interfaces (`Printer`, `Scanner`). |
| **D - Dependency Inversion** | Depend on abstractions, not on concrete classes. | Direct `new / Class()` instantiation in constructors. | Inversion of Control (IoC), Dependency Injection (`Depends()`). |

---

## 5-Minute FAANG Interview Checklist
When given an LLD problem (e.g. *Design a Parking Lot* or *Design a Splitwise*):
1. **Identify Actors & Entities**: Start with single-responsibility models (`User`, `Spot`, `Vehicle`).
2. **Abstract Extensible Points (OCP)**: Where will new features be added? (e.g. `FeeCalculationStrategy`, `PaymentGateway`).
3. **Verify Hierarchies (LSP)**: If `FourWheelerSpot` extends `ParkingSpot`, can it handle any vehicle that fits?
4. **Lean Interfaces (ISP)**: Don't force `Bike` to have a `check_electric_charging()` method.
5. **Invert Dependencies (DIP)**: Inject repositories and strategies into managers and services.
