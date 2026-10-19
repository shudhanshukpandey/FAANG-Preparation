# Facade Pattern

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.


## Overview
- **Intent**: Provide a unified, high-level interface to a set of interfaces in a complex subsystem. Facade defines a simpler interface that makes the subsystem easier to use.
- **Classification**: Structural Pattern.
- **Problem It Solves**: In a complex backend with 5 micro-libraries (Inventory, Payment, Shipping, Accounting, Notification), clients shouldn't need to coordinate 10 API calls in the correct sequence. The Facade provides a single `order_facade.place_order(...)` entry point.

## Architecture & Data Flow

```mermaid
graph TD
    Client[Web / Mobile Client] --> OrderFacade[OrderFulfillmentFacade]

    subgraph Subsystem [Complex Internal Subsystems]
        OrderFacade --> InventoryService[InventoryService: reserve_stock()]
        OrderFacade --> PaymentService[PaymentService: charge_customer()]
        OrderFacade --> ShippingService[ShippingService: book_courier()]
        OrderFacade --> NotificationService[NotificationService: send_sms()]
    end
```

## FAANG Interview Significance
- Essential for API Gateways, backend-for-frontend (BFF) layers, and orchestrating microservice transactions.
- Provides loose coupling: if the Shipping vendor changes from FedEx to DHL, only the `Facade` changes, while API controllers remain untouched.
