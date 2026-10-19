# High-Level Design (HLD) & Distributed Systems Curriculum

An end-to-end curriculum for High-Level System Design, distributed systems architectures, and modern 2026 FAANG engineering standards.

Each module includes:
1. **Interactive Animated Architecture Diagram** (`diagram.html` rendered via [Archify](file:///Users/shudhanshu/.agents/skills/archify/SKILL.md) with theme toggles and export capabilities).
2. **Runnable Python Architecture Simulation** (`<module_name>.py` implemented using the Python standard library with zero third-party dependencies).
3. **Comprehensive Deep-Dive Engineering Guide** (`README.md` covering trade-offs, real-world FAANG case studies, formulas, and edge cases).

---

## 🏃 Master Test Runner

To execute all 62 system design architectural simulations at once:

```bash
python3 "high level design/high_level_design.py"
```

---

## 🗺️ Curriculum Pillars & Modules

### 01. Core Distributed Systems Concepts
| Concept | Code | Interactive Diagram |
| :--- | :--- | :--- |
| **Scalability (Vertical vs Horizontal)** | [scalability.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/01_core_concepts/scalability/scalability.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/01_core_concepts/scalability/diagram.html) |
| **Availability & SLAs (99.9% to 99.999%)** | [availability_and_sla.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/01_core_concepts/availability_and_sla/availability_and_sla.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/01_core_concepts/availability_and_sla/diagram.html) |
| **Latency, Throughput & Bandwidth** | [latency_throughput_bandwidth.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/01_core_concepts/latency_throughput_bandwidth/latency_throughput_bandwidth.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/01_core_concepts/latency_throughput_bandwidth/diagram.html) |
| **CAP Theorem & PACELC** | [cap_and_pacelc.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/01_core_concepts/cap_and_pacelc/cap_and_pacelc.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/01_core_concepts/cap_and_pacelc/diagram.html) |
| **Consistent Hashing & Virtual Nodes** | [consistent_hashing.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/01_core_concepts/consistent_hashing/consistent_hashing.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/01_core_concepts/consistent_hashing/diagram.html) |

### 02. Networking & Traffic Routing
| Concept | Code | Interactive Diagram |
| :--- | :--- | :--- |
| **TCP vs UDP & Connection Handshakes** | [tcp_vs_udp.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/02_networking_and_traffic/tcp_vs_udp/tcp_vs_udp.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/02_networking_and_traffic/tcp_vs_udp/diagram.html) |
| **HTTP Evolution (HTTP/1.1, HTTP/2, HTTP/3 QUIC)** | [http_evolution.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/02_networking_and_traffic/http_evolution/http_evolution.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/02_networking_and_traffic/http_evolution/diagram.html) |
| **DNS Resolution & Anycast BGP Routing** | [dns_and_anycast.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/02_networking_and_traffic/dns_and_anycast/dns_and_anycast.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/02_networking_and_traffic/dns_and_anycast/diagram.html) |
| **Forward Proxy vs Reverse Proxy** | [forward_vs_reverse_proxy.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/02_networking_and_traffic/forward_vs_reverse_proxy/forward_vs_reverse_proxy.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/02_networking_and_traffic/forward_vs_reverse_proxy/diagram.html) |

### 03. Load Balancing & Traffic Distribution
| Concept | Code | Interactive Diagram |
| :--- | :--- | :--- |
| **L4 vs L7 & Load Balancing Algorithms** | [load_balancing_algorithms.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/03_load_balancing/load_balancing_algorithms/load_balancing_algorithms.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/03_load_balancing/load_balancing_algorithms/diagram.html) |
| **Health Checking & Automatic Failover** | [health_checking_and_failover.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/03_load_balancing/health_checking_and_failover/health_checking_and_failover.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/03_load_balancing/health_checking_and_failover/diagram.html) |

### 04. API Design, Gateways & Security
| Concept | Code | Interactive Diagram |
| :--- | :--- | :--- |
| **REST vs GraphQL vs gRPC** | [rest_vs_graphql_vs_grpc.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/04_api_design_and_gateways/rest_vs_graphql_vs_grpc/rest_vs_graphql_vs_grpc.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/04_api_design_and_gateways/rest_vs_graphql_vs_grpc/diagram.html) |
| **Idempotency Keys & Distributed Deduplication** | [idempotency_patterns.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/04_api_design_and_gateways/idempotency_patterns/idempotency_patterns.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/04_api_design_and_gateways/idempotency_patterns/diagram.html) |
| **API Gateway (Routing, Rate Limiting, SSL Offloading)** | [api_gateway.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/04_api_design_and_gateways/api_gateway/api_gateway.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/04_api_design_and_gateways/api_gateway/diagram.html) |
| **Authentication: JWT, OAuth 2.0 & Session Stores** | [auth_and_tokens.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/04_api_design_and_gateways/auth_and_tokens/auth_and_tokens.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/04_api_design_and_gateways/auth_and_tokens/diagram.html) |

### 05. Asynchronous & Real-Time Communication
| Concept | Code | Interactive Diagram |
| :--- | :--- | :--- |
| **Polling vs Long-Polling vs WebSockets vs SSE** | [real_time_communication.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/05_communication_patterns/real_time_communication/real_time_communication.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/05_communication_patterns/real_time_communication/diagram.html) |
| **Message Queues: RabbitMQ vs Apache Kafka** | [message_queues.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/05_communication_patterns/message_queues/message_queues.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/05_communication_patterns/message_queues/diagram.html) |
| **Pub/Sub, Topic Fanout & Dead Letter Queues (DLQ)** | [pub_sub_and_dlq.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/05_communication_patterns/pub_sub_and_dlq/pub_sub_and_dlq.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/05_communication_patterns/pub_sub_and_dlq/diagram.html) |

### 06. Caching Strategies & Performance
| Concept | Code | Interactive Diagram |
| :--- | :--- | :--- |
| **Caching Patterns (Cache-Aside, Write-Through, Write-Behind)** | [caching_patterns.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/06_caching_strategies/caching_patterns/caching_patterns.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/06_caching_strategies/caching_patterns/diagram.html) |
| **Cache Eviction Policies (LRU, LFU, FIFO, ARC)** | [eviction_policies.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/06_caching_strategies/eviction_policies/eviction_policies.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/06_caching_strategies/eviction_policies/diagram.html) |
| **Content Delivery Networks (CDN) & Edge Caching** | [cdn_architecture.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/06_caching_strategies/cdn_architecture/cdn_architecture.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/06_caching_strategies/cdn_architecture/diagram.html) |
| **Cache Stampede, Penetration & Proactive Warming** | [cache_stampede_and_warming.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/06_caching_strategies/cache_stampede_and_warming/cache_stampede_and_warming.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/06_caching_strategies/cache_stampede_and_warming/diagram.html) |

### 07. Database Architectures & Storage Engines
| Concept | Code | Interactive Diagram |
| :--- | :--- | :--- |
| **SQL vs NoSQL (Document, Key-Value, Columnar, Graph)** | [sql_vs_nosql.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/07_database_architectures/sql_vs_nosql/sql_vs_nosql.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/07_database_architectures/sql_vs_nosql/diagram.html) |
| **ACID vs BASE (Eventual Consistency & Isolation Levels)** | [acid_vs_base.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/07_database_architectures/acid_vs_base/acid_vs_base.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/07_database_architectures/acid_vs_base/diagram.html) |
| **Storage Engines: B+ Tree vs LSM-Tree** | [b_plus_tree_vs_lsm_tree.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/07_database_architectures/b_plus_tree_vs_lsm_tree/b_plus_tree_vs_lsm_tree.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/07_database_architectures/b_plus_tree_vs_lsm_tree/diagram.html) |
| **Specialized Databases (Time-Series, Graph & Vector DBs)** | [specialized_databases.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/07_database_architectures/specialized_databases/specialized_databases.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/07_database_architectures/specialized_databases/diagram.html) |

### 08. Database Scaling & Operations
| Concept | Code | Interactive Diagram |
| :--- | :--- | :--- |
| **Read Replication & Replication Lag Mitigation** | [read_replication.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/08_database_scaling/read_replication/read_replication.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/08_database_scaling/read_replication/diagram.html) |
| **Sharding & Partitioning (Hash vs Range vs Directory)** | [sharding_and_partitioning.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/08_database_scaling/sharding_and_partitioning/sharding_and_partitioning.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/08_database_scaling/sharding_and_partitioning/diagram.html) |
| **Database Connection Pooling (PgBouncer, HikariCP)** | [connection_pooling.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/08_database_scaling/connection_pooling/connection_pooling.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/08_database_scaling/connection_pooling/diagram.html) |

### 09. Storage Systems & Durability
| Concept | Code | Interactive Diagram |
| :--- | :--- | :--- |
| **Block vs File vs Object Storage (S3 / GCS)** | [block_file_object_storage.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/09_storage_systems/block_file_object_storage/block_file_object_storage.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/09_storage_systems/block_file_object_storage/diagram.html) |
| **Erasure Coding & Reed-Solomon Durability** | [erasure_coding.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/09_storage_systems/erasure_coding/erasure_coding.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/09_storage_systems/erasure_coding/diagram.html) |

### 10. Architectural Paradigms & Patterns
| Concept | Code | Interactive Diagram |
| :--- | :--- | :--- |
| **Monolith vs Microservices vs Serverless** | [monolith_vs_microservices_vs_serverless.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/10_architectural_patterns/monolith_vs_microservices_vs_serverless/monolith_vs_microservices_vs_serverless.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/10_architectural_patterns/monolith_vs_microservices_vs_serverless/diagram.html) |
| **Event-Driven Architecture (Orchestration vs Choreography)** | [event_driven_architecture.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/10_architectural_patterns/event_driven_architecture/event_driven_architecture.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/10_architectural_patterns/event_driven_architecture/diagram.html) |
| **CQRS (Command Query Responsibility Segregation)** | [cqrs.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/10_architectural_patterns/cqrs/cqrs.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/10_architectural_patterns/cqrs/diagram.html) |
| **Event Sourcing & State Projections** | [event_sourcing.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/10_architectural_patterns/event_sourcing/event_sourcing.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/10_architectural_patterns/event_sourcing/diagram.html) |

### 11. Microservices Resilience & Migration
| Concept | Code | Interactive Diagram |
| :--- | :--- | :--- |
| **Service Discovery (Consul, Eureka, DNS-SD)** | [service_discovery.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/11_microservices_resilience/service_discovery/service_discovery.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/11_microservices_resilience/service_discovery/diagram.html) |
| **BFF (Backend-for-Frontend) & Sidecar Pattern** | [bff_and_sidecar.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/11_microservices_resilience/bff_and_sidecar/bff_and_sidecar.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/11_microservices_resilience/bff_and_sidecar/diagram.html) |
| **Bulkhead Pattern & Strangler Fig Migration** | [bulkhead_and_strangler_fig.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/11_microservices_resilience/bulkhead_and_strangler_fig/bulkhead_and_strangler_fig.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/11_microservices_resilience/bulkhead_and_strangler_fig/diagram.html) |

### 12. Distributed Consensus & Coordination
| Concept | Code | Interactive Diagram |
| :--- | :--- | :--- |
| **Logical Clocks (Lamport & Vector Clocks)** | [logical_clocks_and_timestamps.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/12_distributed_consensus/logical_clocks_and_timestamps/logical_clocks_and_timestamps.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/12_distributed_consensus/logical_clocks_and_timestamps/diagram.html) |
| **Leader Election & Heartbeat Liveness** | [leader_election_and_heartbeats.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/12_distributed_consensus/leader_election_and_heartbeats/leader_election_and_heartbeats.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/12_distributed_consensus/leader_election_and_heartbeats/diagram.html) |
| **Distributed Locks & Fencing Tokens** | [distributed_locks.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/12_distributed_consensus/distributed_locks/distributed_locks.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/12_distributed_consensus/distributed_locks/diagram.html) |
| **Raft Distributed Consensus (Election & Replication)** | [raft_consensus.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/12_distributed_consensus/raft_consensus/raft_consensus.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/12_distributed_consensus/raft_consensus/diagram.html) |
| **Gossip Protocol & CRDTs** | [gossip_protocol_and_crdts.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/12_distributed_consensus/gossip_protocol_and_crdts/gossip_protocol_and_crdts.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/12_distributed_consensus/gossip_protocol_and_crdts/diagram.html) |

### 13. Distributed Transactions & Workflows
| Concept | Code | Interactive Diagram |
| :--- | :--- | :--- |
| **Two-Phase Commit (2PC) & Coordinator Failures** | [two_phase_commit_2pc.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/13_distributed_transactions/two_phase_commit_2pc/two_phase_commit_2pc.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/13_distributed_transactions/two_phase_commit_2pc/diagram.html) |
| **Saga Pattern (Compensating Transactions)** | [saga_pattern.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/13_distributed_transactions/saga_pattern/saga_pattern.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/13_distributed_transactions/saga_pattern/diagram.html) |

### 14. Data Structures for Extreme Scale
| Concept | Code | Interactive Diagram |
| :--- | :--- | :--- |
| **Bloom & Cuckoo Filters** | [bloom_and_cuckoo_filters.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/14_data_structures_for_scale/bloom_and_cuckoo_filters/bloom_and_cuckoo_filters.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/14_data_structures_for_scale/bloom_and_cuckoo_filters/diagram.html) |
| **HyperLogLog & Count-Min Sketch** | [hyperloglog_and_count_min.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/14_data_structures_for_scale/hyperloglog_and_count_min/hyperloglog_and_count_min.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/14_data_structures_for_scale/hyperloglog_and_count_min/diagram.html) |
| **Geohashing & Quadtrees** | [geohash_and_quadtree.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/14_data_structures_for_scale/geohash_and_quadtree/geohash_and_quadtree.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/14_data_structures_for_scale/geohash_and_quadtree/diagram.html) |
| **Merkle Trees & Anti-Entropy Repair** | [merkle_tree.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/14_data_structures_for_scale/merkle_tree/merkle_tree.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/14_data_structures_for_scale/merkle_tree/diagram.html) |

### 15. Big Data & Streaming Architectures
| Concept | Code | Interactive Diagram |
| :--- | :--- | :--- |
| **Batch vs Stream Processing Trade-Offs** | [batch_vs_stream_processing.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/15_big_data_and_streaming/batch_vs_stream_processing/batch_vs_stream_processing.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/15_big_data_and_streaming/batch_vs_stream_processing/diagram.html) |
| **MapReduce Distributed Processing Pipeline** | [mapreduce_pipeline.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/15_big_data_and_streaming/mapreduce_pipeline/mapreduce_pipeline.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/15_big_data_and_streaming/mapreduce_pipeline/diagram.html) |
| **Change Data Capture (CDC) & The Outbox Pattern** | [change_data_capture_cdc.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/15_big_data_and_streaming/change_data_capture_cdc/change_data_capture_cdc.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/15_big_data_and_streaming/change_data_capture_cdc/diagram.html) |
| **Lambda vs Kappa Architecture** | [lambda_vs_kappa_architecture.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/15_big_data_and_streaming/lambda_vs_kappa_architecture/lambda_vs_kappa_architecture.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/15_big_data_and_streaming/lambda_vs_kappa_architecture/diagram.html) |

### 16. Deployment, Configuration & Observability
| Concept | Code | Interactive Diagram |
| :--- | :--- | :--- |
| **Canary & Blue-Green Deployments** | [deployment_strategies.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/16_deployment_and_observability/deployment_strategies/deployment_strategies.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/16_deployment_and_observability/deployment_strategies/diagram.html) |
| **Dynamic Feature Flags & Kill Switches** | [feature_flags.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/16_deployment_and_observability/feature_flags/feature_flags.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/16_deployment_and_observability/feature_flags/diagram.html) |
| **Distributed Tracing (OpenTelemetry) & RED Metrics** | [distributed_tracing_and_metrics.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/16_deployment_and_observability/distributed_tracing_and_metrics/distributed_tracing_and_metrics.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/16_deployment_and_observability/distributed_tracing_and_metrics/diagram.html) |

### 17. Security, Cryptography & Identity
| Concept | Code | Interactive Diagram |
| :--- | :--- | :--- |
| **TLS 1.3 & Envelope Encryption at Rest** | [tls_and_encryption.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/17_security_and_identity/tls_and_encryption/tls_and_encryption.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/17_security_and_identity/tls_and_encryption/diagram.html) |
| **Secrets Management (Vault) & Key Rotation** | [secrets_and_key_rotation.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/17_security_and_identity/secrets_and_key_rotation/secrets_and_key_rotation.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/17_security_and_identity/secrets_and_key_rotation/diagram.html) |
| **RBAC & Attribute-Based Access Control (ABAC)** | [rbac_and_access_control.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/17_security_and_identity/rbac_and_access_control/rbac_and_access_control.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/17_security_and_identity/rbac_and_access_control/diagram.html) |

### 18. Modern AI & LLM Infrastructure (2026 FAANG Standards)
| Concept | Code | Interactive Diagram |
| :--- | :--- | :--- |
| **Retrieval-Augmented Generation (RAG) Architecture** | [rag_pipeline.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/18_ai_and_llm_infrastructure/rag_pipeline/rag_pipeline.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/18_ai_and_llm_infrastructure/rag_pipeline/diagram.html) |
| **LLM Inference Serving & Continuous Batching** | [llm_inference_serving.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/18_ai_and_llm_infrastructure/llm_inference_serving/llm_inference_serving.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/18_ai_and_llm_infrastructure/llm_inference_serving/diagram.html) |
| **Vector Database Internals (HNSW & Quantization)** | [vector_database_internals.py](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/18_ai_and_llm_infrastructure/vector_database_internals/vector_database_internals.py) | [diagram.html](file:///Users/shudhanshu/Desktop/FAANG-Preparation/high%20level%20design/18_ai_and_llm_infrastructure/vector_database_internals/diagram.html) |
