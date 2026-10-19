# Expense Sharing System (Splitwise)

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

## Overview
- **Intent**: Manage shared group and individual expenses with multiple splitting strategies, maintaining an exact ledger and minimizing settlement transactions using debt simplification.
- **Classification**: Classic Machine Coding / Financial Ledger.
- **Real-World Parallels**: Splitwise, Tricount, Venmo Groups.

## Core Features
1. **Split Strategies**:
   - `EQUAL`: Splits the bill equally across all participants with rounding delta adjustments.
   - `EXACT`: Specifies precise per-person dollar amounts with total validation.
   - `PERCENT`: Allocates expenses by percentage, validating that the sum equals 100%.
2. **Min-Cash-Flow Debt Simplification**:
   - Computes net balance across all participants (`Creditors` vs `Debtors`).
   - Uses a two-pointer greedy balance resolution to settle maximal debts in a minimal number of transactions (reducing an $O(N^2)$ transaction mesh to at most $N-1$ payments).
