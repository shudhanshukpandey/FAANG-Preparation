# Distributed Task Scheduler & Job Runner

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

## Overview
- **Intent**: Manage delayed and scheduled background task execution across concurrent worker pools with lease-based locking, exponential backoff retries, and dead-letter queuing.
- **Classification**: Classic Machine Coding / Distributed Systems.
- **Real-World Parallels**: Celery, Temporal, Quartz, AWS SQS with Lambda.

## Core Features
1. **Priority Heap by Timestamp**: Orders scheduled tasks by `run_at` Unix epoch for $O(\log N)$ insertion and $O(1)$ head peek.
2. **Worker Leasing**: Workers acquire an exclusive lock upon polling, transitioning task state from `PENDING` to `RUNNING`.
3. **Exponential Backoff**: Failed tasks double their retry delay before being re-inserted into the priority queue.
4. **Dead Letter Queue (DLQ)**: Tasks that exhaust all retry attempts are quarantined in a DLQ for operational triage.
