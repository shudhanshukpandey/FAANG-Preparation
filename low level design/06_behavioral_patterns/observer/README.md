# Observer Pattern

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.


## Overview
- **Intent**: Define a one-to-many dependency between objects so that when one object (Subject / Observable) changes state, all its dependents (Observers / Subscribers) are automatically notified and updated.
- **Classification**: Behavioral Pattern (Pub-Sub).
- **Core Components**:
  - **Subject / Publisher**: Maintains a collection of observers; provides `subscribe()`, `unsubscribe()`, and `notify_observers()`.
  - **Observer / Subscriber**: Defines an `update(state)` interface called when changes occur.

## Architecture & Data Flow

```mermaid
classDiagram
    class StockMarketTicker {
        -dict _observers
        -dict _prices
        +subscribe(symbol: str, observer: StockObserver)
        +unsubscribe(symbol: str, observer: StockObserver)
        +update_price(symbol: str, new_price: float)
        -_notify(symbol: str, price: float)
    }

    class StockObserver {
        <<interface>>
        +on_price_change(symbol: str, price: float)*
    }

    class MobileAppSubscriber {
        +on_price_change(symbol: str, price: float)
    }

    class AlgorithmicTradingBot {
        +on_price_change(symbol: str, price: float)
    }

    StockObserver <|.. MobileAppSubscriber : realizes
    StockObserver <|.. AlgorithmicTradingBot : realizes
    StockMarketTicker o-- StockObserver : notifies 1-to-many
```

## FAANG Interview Significance
- High-yield pattern in system design: Event-driven notification hubs, WebSocket price tickers, UI event listeners, and In-Memory Pub/Sub messaging.
