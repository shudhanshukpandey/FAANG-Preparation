# UML Activity Diagram

## Overview
An **Activity Diagram** describes the workflow of a system, modeling control flow, logic branching, and concurrent operations:
- **Initial State (Filled Circle)**: Workflow entry point.
- **Action State (Rounded Rectangle)**: An execution step (e.g. "Validate Card").
- **Decision Node (Diamond)**: Conditional branching with guards (`[balance >= amount]`).
- **Fork Bar**: Splits a single flow into multiple concurrent parallel threads.
- **Join Bar**: Synchronizes concurrent flows before proceeding.
- **Final State (Bullseye / Bordered Circle)**: Workflow completion.

## Architecture & Data Flow: ATM Withdrawal Workflow

```mermaid
stateDiagram-v2
    [*] --> InsertCard
    InsertCard --> EnterPIN
    EnterPIN --> ValidatePIN

    state check_pin <<choice>>
    ValidatePIN --> check_pin
    check_pin --> SelectAmount : [PIN Valid]
    check_pin --> EjectCard : [PIN Invalid 3 times]
    EjectCard --> [*]

    SelectAmount --> CheckAccountBalance

    state check_balance <<choice>>
    CheckAccountBalance --> check_balance
    check_balance --> ParallelDispense : [Sufficient Balance]
    check_balance --> DisplayError : [Insufficient Balance]
    DisplayError --> EjectCard

    state ParallelDispense {
        state fork_node <<fork>>
        state join_node <<join>>

        [*] --> fork_node
        fork_node --> DispenseCash : Thread 1
        fork_node --> PrintReceipt : Thread 2
        fork_node --> UpdateDatabase : Thread 3

        DispenseCash --> join_node
        PrintReceipt --> join_node
        UpdateDatabase --> join_node
        join_node --> [*]
    }

    ParallelDispense --> ReturnCard
    ReturnCard --> [*]
```

## FAANG LLD Interview Tips
- Great for illustrating concurrency and background jobs (e.g., when an order is placed, simultaneously charge card, update search index, and dispatch Kafka event via fork/join).
