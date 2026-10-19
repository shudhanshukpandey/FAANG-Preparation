# Saga Pattern (Compensating Transactions)

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

- **Eventual Consistency**: Replaces blocking 2PC locks with local transactions.
- **Compensating Action**: If step $N$ fails, rollback steps $N-1 \dots 1$ via semantic reverse operations (e.g. Refund Payment).
