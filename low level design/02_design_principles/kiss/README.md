# Keep It Simple, Stupid (KISS)

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.


## Overview
- **KISS Principle**: Systems perform best when kept simple rather than made complicated.
- **Overengineering (Anti-Pattern)**: Building 6 layers of abstract factories, dynamic proxies, and generic reflection to solve a straightforward requirement (e.g. checking if a string is a palindrome or generating a greeting).
- **Core Rule**: Avoid premature cleverness. Write code that is easy to read, test, and maintain.

## Architecture & Data Flow

```mermaid
graph TD
    subgraph Overengineered [Anti-Pattern: 5 Layers of Indirection]
        Input[Input String] --> Factory[StringReversalFactoryProvider]
        Factory --> Strategy[IStringTransformationStrategy]
        Strategy --> Context[ReversalExecutionContext]
        Context --> Validator[AbstractValidationOrchestrator]
        Validator --> Output[Output: Boolean]
    end

    subgraph Simple [KISS Refactored]
        InputSimple[Input String] --> BuiltinFunction[Clean Python Slice: s == s[::-1]]
        BuiltinFunction --> OutputSimple[Output: Boolean]
    end
```

## FAANG Interview Significance
- Interviewers penalize candidates who over-complicate 45-minute coding rounds with unnecessary design patterns when simple, direct functions solve the problem cleanly.
