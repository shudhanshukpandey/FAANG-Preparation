# Low-Level Design (LLD) & Object-Oriented Design (OOD) Master Guide

Welcome to the comprehensive Low-Level Design repository. This repository is structured to bridge theoretical object-oriented fundamentals, GoF design patterns, production backend architecture (FastAPI, Flask, Django), and end-to-end FAANG machine coding rounds.

> [!TIP]
> **Interactive Animated Data Flows (Archify)**:
> Every pattern and fundamental module directory contains a dedicated **`diagram.html`** and **`diagram.dataflow.json`** created with **Archify**.
> You can open any `diagram.html` directly in your browser to inspect interactive stage pipelines, animated packet pulses, dark/light theme switching, and vector SVG export.

---

## 📚 Curriculum Roadmap

```
low level design/
├── 01_oop_fundamentals/             # Core Object-Oriented Principles & Relationships
├── 02_design_principles/            # DRY, KISS, YAGNI, LoD, and complete SOLID deep-dive
├── 03_uml_modeling/                 # Class, Sequence, Use Case, Activity & State diagrams (Mermaid)
├── 04_creational_patterns/          # Singleton, Factory Method, Abstract Factory, Builder, Prototype
├── 05_structural_patterns/          # Adapter, Facade, Decorator, Composite, Proxy, Bridge, Flyweight
├── 06_behavioral_patterns/          # Strategy, Observer, Command, State, Chain of Responsibility, etc.
├── 07_enterprise_backend_patterns/  # Repository, Service Layer, Unit of Work, DI, DTO, Middleware, Outbox
├── 08_resilience_and_concurrency/   # Rate Limiter, Circuit Breaker, Object Pool, Concurrency Locking
└── 09_classic_machine_coding/       # End-to-end problems (Parking Lot, LRU Cache, Rate Limiter, etc.)
```

---

## 🎯 Quick Navigation & Index

### 1. OOP Fundamentals (`01_oop_fundamentals/`)
- [Classes & Objects](01_oop_fundamentals/classes_and_objects/README.md) (`classes_and_objects.py`)
- [Interfaces & Protocols](01_oop_fundamentals/interfaces_and_protocols/README.md) (`interfaces_and_protocols.py`)
- [Inheritance](01_oop_fundamentals/inheritance/README.md) (`inheritance.py`)
- [Polymorphism](01_oop_fundamentals/polymorphism/README.md) (`polymorphism.py`)
- [Abstraction](01_oop_fundamentals/abstraction/README.md) (`abstraction.py`)
- [Encapsulation](01_oop_fundamentals/encapsulation/README.md) (`encapsulation.py`)
- [Association](01_oop_fundamentals/association/README.md) (`association.py`)
- [Aggregation](01_oop_fundamentals/aggregation/README.md) (`aggregation.py`)
- [Composition](01_oop_fundamentals/composition/README.md) (`composition.py`)

### 2. Design Principles (`02_design_principles/`)
- [DRY (Don't Repeat Yourself)](02_design_principles/dry/README.md) (`dry.py`)
- [KISS (Keep It Simple Stupid)](02_design_principles/kiss/README.md) (`kiss.py`)
- [YAGNI (You Aren't Gonna Need It)](02_design_principles/yagni/README.md) (`yagni.py`)
- [Law of Demeter (LoD)](02_design_principles/lod/README.md) (`lod.py`)
- [Single Responsibility Principle (SRP)](02_design_principles/srp/README.md) (`srp.py`)
- [Open/Closed Principle (OCP)](02_design_principles/ocp/README.md) (`ocp.py`)
- [Liskov Substitution Principle (LSP)](02_design_principles/lsp/README.md) (`lsp.py`)
- [Interface Segregation Principle (ISP)](02_design_principles/isp/README.md) (`isp.py`)
- [Dependency Inversion Principle (DIP)](02_design_principles/dip/README.md) (`dip.py`)
- [SOLID Principles Summary & Cheat Sheet](02_design_principles/solid_summary/README.md)

### 3. UML Modeling (`03_uml_modeling/`)
- [Class Diagram](03_uml_modeling/class_diagram/README.md)
- [Use Case Diagram](03_uml_modeling/use_case_diagram/README.md)
- [Sequence Diagram](03_uml_modeling/sequence_diagram/README.md)
- [Activity Diagram](03_uml_modeling/activity_diagram/README.md)
- [State Machine Diagram](03_uml_modeling/state_machine_diagram/README.md)

### 4. Creational Patterns (`04_creational_patterns/`)
- [Singleton](04_creational_patterns/singleton/README.md) (`singleton.py`)
- [Factory Method](04_creational_patterns/factory_method/README.md) (`factory_method.py`)
- [Abstract Factory](04_creational_patterns/abstract_factory/README.md) (`abstract_factory.py`)
- [Builder](04_creational_patterns/builder/README.md) (`builder.py`)
- [Prototype](04_creational_patterns/prototype/README.md) (`prototype.py`)

### 5. Structural Patterns (`05_structural_patterns/`)
- [Adapter](05_structural_patterns/adapter/README.md) (`adapter.py`)
- [Facade](05_structural_patterns/facade/README.md) (`facade.py`)
- [Decorator](05_structural_patterns/decorator/README.md) (`decorator.py`)
- [Composite](05_structural_patterns/composite/README.md) (`composite.py`)
- [Proxy](05_structural_patterns/proxy/README.md) (`proxy.py`)
- [Bridge](05_structural_patterns/bridge/README.md) (`bridge.py`)
- [Flyweight](05_structural_patterns/flyweight/README.md) (`flyweight.py`)

### 6. Behavioral Patterns (`06_behavioral_patterns/`)
- [Strategy](06_behavioral_patterns/strategy/README.md) (`strategy.py`)
- [Observer](06_behavioral_patterns/observer/README.md) (`observer.py`)
- [Command](06_behavioral_patterns/command/README.md) (`command.py`)
- [State](06_behavioral_patterns/state/README.md) (`state.py`)
- [Chain of Responsibility](06_behavioral_patterns/chain_of_responsibility/README.md) (`chain_of_responsibility.py`)
- [Template Method](06_behavioral_patterns/template_method/README.md) (`template_method.py`)
- [Iterator](06_behavioral_patterns/iterator/README.md) (`iterator.py`)
- [Mediator](06_behavioral_patterns/mediator/README.md) (`mediator.py`)
- [Memento](06_behavioral_patterns/memento/README.md) (`memento.py`)
- [Visitor](06_behavioral_patterns/visitor/README.md) (`visitor.py`)

### 7. Enterprise Backend Patterns (`07_enterprise_backend_patterns/`)
*(Tailored for FastAPI, Flask, and Django architectures)*
- [Repository Pattern](07_enterprise_backend_patterns/repository/README.md) (`repository.py`)
- [Service Layer Pattern](07_enterprise_backend_patterns/service_layer/README.md) (`service_layer.py`)
- [Unit of Work (UoW)](07_enterprise_backend_patterns/unit_of_work/README.md) (`unit_of_work.py`)
- [Dependency Injection](07_enterprise_backend_patterns/dependency_injection/README.md) (`dependency_injection.py`)
- [DTO & Value Objects](07_enterprise_backend_patterns/dto_and_value_objects/README.md) (`dto_and_value_objects.py`)
- [Middleware Pipeline](07_enterprise_backend_patterns/middleware_pipeline/README.md) (`middleware_pipeline.py`)
- [Transactional Outbox](07_enterprise_backend_patterns/transactional_outbox/README.md) (`transactional_outbox.py`)

### 8. Resilience & Concurrency Patterns (`08_resilience_and_concurrency/`)
- [Rate Limiter (Token Bucket & Sliding Window)](08_resilience_and_concurrency/rate_limiter/README.md) (`rate_limiter.py`)
- [Circuit Breaker](08_resilience_and_concurrency/circuit_breaker/README.md) (`circuit_breaker.py`)
- [Object Pool / Connection Pool](08_resilience_and_concurrency/object_pool/README.md) (`object_pool.py`)
- [Concurrency & Locking (Optimistic vs. Pessimistic)](08_resilience_and_concurrency/concurrency_locking/README.md) (`concurrency_locking.py`)

### 9. Classic FAANG Machine Coding Case Studies (`09_classic_machine_coding/`)
- [LRU Cache System](09_classic_machine_coding/lru_cache/README.md) (`lru_cache.py`)
- [Parking Lot System](09_classic_machine_coding/parking_lot/README.md) (`parking_lot.py`)
- [Rate Limiter Service](09_classic_machine_coding/rate_limiter_service/README.md) (`rate_limiter_service.py`)
- [Snake & Ladder Game](09_classic_machine_coding/snake_and_ladder/README.md) (`snake_and_ladder.py`)
- [Notification Service](09_classic_machine_coding/notification_service/README.md) (`notification_service.py`)

---

## 💡 How to Use This Repository
Each subfolder is an independent module containing:
1. `README.md`: High-level explanation, visual diagrams (Mermaid sequence/class diagrams + ASCII fallback), framework contexts, and FAANG interview takeaways.
2. `<name>.py`: Self-contained runnable Python 3 code using Python standard library with complete type annotations.
