# In-Memory Key-Value Store (Mini-Redis)

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

## Overview
- **Intent**: Implement an in-memory key-value data store supporting strings, hashes, time-to-live (TTL) expiration, and atomic multi-operation transactions.
- **Classification**: Classic Machine Coding / Storage Engine.
- **Real-World Parallels**: Redis, Memcached, Dragonfly.

## Core Features
1. **String Operations**: `SET(key, val, ttl)`, `GET(key)`, `DEL(key)`.
2. **Hash Operations**: `HSET(key, field, val)`, `HGET(key, field)`, `HGETALL(key)`.
3. **TTL & Expiration**: Passive expiration on read access + active background sweeps.
4. **Transactions (MULTI / EXEC / DISCARD)**: Queue commands within a connection and execute atomically under a re-entrant lock.

## Key Design Decisions
- **Locking Granularity**: An `RLock` synchronizes updates to the underlying hash table, with thread-local storage tracking ongoing queued transactions without contaminating concurrent worker threads.
- **Passive Expiration**: Upon every `get()` or `hget()`, the key expiration timestamp is inspected. If expired, it is immediately pruned and `None` is returned, avoiding stale reads.
