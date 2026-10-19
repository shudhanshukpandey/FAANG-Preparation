# Don't Repeat Yourself (DRY)

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.


## Overview
- **DRY Principle**: "Every piece of knowledge must have a single, unambiguous, authoritative representation within a system."
- **WET Code (Anti-Pattern)**: "We Enjoy Typing" or "Write Everything Twice" — duplicating business logic, validation rules, or database queries across multiple controllers/services.
- **The Balance**: Avoid "Accidental Duplication" (code that looks similar today but represents different domain concepts and will diverge tomorrow).

## Architecture & Data Flow

```mermaid
graph TD
    subgraph WET [Anti-Pattern: Duplicated Tax Calculations]
        ControllerA[Invoicing Controller] --> Calc1[Duplicate Tax & Discount Logic]
        ControllerB[Cart Checkout] --> Calc2[Duplicate Tax & Discount Logic]
        ControllerC[Mobile Order API] --> Calc3[Duplicate Tax & Discount Logic]
    end

    subgraph DRY [Refactored: Single Source of Truth]
        API_A[Invoicing Controller] --> TaxService[TaxCalculator Service]
        API_B[Cart Checkout] --> TaxService
        API_C[Mobile Order API] --> TaxService
    end
```

## FAANG Interview Significance
- Bugs occur when tax/discount/auth rules change in one place but developers forget to update the 3 other duplicate places.
- In FastAPI/Flask/Django: Encapsulating validation in Pydantic validators, Django custom model managers, or shared service layers.
