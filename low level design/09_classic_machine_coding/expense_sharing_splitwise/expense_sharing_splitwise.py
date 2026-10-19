"""Expense Sharing System (Splitwise).

Features:
- User balances across groups and individual accounts.
- Flexible Expense Splits: EQUAL, EXACT, and PERCENTAGE.
- Debt Simplification Algorithm (Min-Cash-Flow greedy graph resolution)
  that minimizes total financial transactions between all users.
"""

from __future__ import annotations

from enum import Enum
from dataclasses import dataclass
from typing import Dict, List, Tuple, Any


class SplitType(Enum):
    EQUAL = "EQUAL"
    EXACT = "EXACT"
    PERCENT = "PERCENT"


@dataclass
class User:
    user_id: str
    name: str


@dataclass
class Split:
    user: User
    amount: float = 0.0
    percentage: float = 0.0


class ExpenseManager:
    def __init__(self) -> None:
        self.users: Dict[str, User] = {}
        # balance_sheet[u1][u2] = amount u1 owes u2 (if positive)
        self.balance_sheet: Dict[str, Dict[str, float]] = {}

    def add_user(self, user_id: str, name: str) -> User:
        user = User(user_id, name)
        self.users[user_id] = user
        self.balance_sheet[user_id] = {}
        return user

    def add_expense(
        self,
        split_type: SplitType,
        total_amount: float,
        paid_by: User,
        splits: List[Split],
    ) -> None:
        if split_type == SplitType.EQUAL:
            share = round(total_amount / len(splits), 2)
            for s in splits:
                s.amount = share
            # Handle rounding delta on first recipient
            delta = round(total_amount - (share * len(splits)), 2)
            splits[0].amount += delta

        elif split_type == SplitType.EXACT:
            total_split = sum(s.amount for s in splits)
            if round(total_split, 2) != round(total_amount, 2):
                raise ValueError("Exact split sum does not match total amount")

        elif split_type == SplitType.PERCENT:
            total_pct = sum(s.percentage for s in splits)
            if round(total_pct, 2) != 100.0:
                raise ValueError("Percentage splits must equal 100%")
            for s in splits:
                s.amount = round((s.percentage * total_amount) / 100.0, 2)

        # Update pairwise ledger
        payer_id = paid_by.user_id
        for s in splits:
            borrower_id = s.user.user_id
            if borrower_id == payer_id:
                continue

            # borrower owes payer
            self.balance_sheet[borrower_id][payer_id] = round(
                self.balance_sheet[borrower_id].get(payer_id, 0.0) + s.amount, 2
            )
            # reverse entry
            self.balance_sheet[payer_id][borrower_id] = round(
                self.balance_sheet[payer_id].get(borrower_id, 0.0) - s.amount, 2
            )

    def get_net_balances(self) -> Dict[str, float]:
        net: Dict[str, float] = {uid: 0.0 for uid in self.users}
        for u1, debts in self.balance_sheet.items():
            for u2, amt in debts.items():
                if amt > 0:
                    net[u1] -= amt
                    net[u2] += amt
        return {uid: round(val, 2) for uid, val in net.items()}

    def simplify_debts(self) -> List[Tuple[str, str, float]]:
        """Min-Cash-Flow algorithm to simplify all debts to minimal transactions."""
        net = self.get_net_balances()

        debtors: List[List[Any]] = []  # [user_id, owed_amount] (negative net)
        creditors: List[List[Any]] = []  # [user_id, credit_amount] (positive net)

        for uid, bal in net.items():
            if bal < -0.01:
                debtors.append([uid, -bal])
            elif bal > 0.01:
                creditors.append([uid, bal])

        transactions: List[Tuple[str, str, float]] = []

        d_idx = 0
        c_idx = 0

        while d_idx < len(debtors) and c_idx < len(creditors):
            debtor_id, debt_amt = debtors[d_idx]
            creditor_id, cred_amt = creditors[c_idx]

            settled = min(debt_amt, cred_amt)
            transactions.append((debtor_id, creditor_id, round(settled, 2)))

            debtors[d_idx][1] -= settled
            creditors[c_idx][1] -= settled

            if debtors[d_idx][1] < 0.01:
                d_idx += 1
            if creditors[c_idx][1] < 0.01:
                c_idx += 1

        return transactions


def run_tests() -> None:
    mgr = ExpenseManager()
    u1 = mgr.add_user("u1", "Alice")
    u2 = mgr.add_user("u2", "Bob")
    u3 = mgr.add_user("u3", "Charlie")

    # Alice pays 300 split equally among Alice, Bob, Charlie
    mgr.add_expense(
        SplitType.EQUAL,
        300.0,
        paid_by=u1,
        splits=[Split(u1), Split(u2), Split(u3)],
    )

    # Bob pays 150 split equally between Bob and Charlie
    mgr.add_expense(
        SplitType.EQUAL,
        150.0,
        paid_by=u2,
        splits=[Split(u2), Split(u3)],
    )

    # Net balances:
    # Alice: +200
    # Bob: -100 + 75 = -25
    # Charlie: -100 - 75 = -175
    net = mgr.get_net_balances()
    assert net["u1"] == 200.0
    assert net["u2"] == -25.0
    assert net["u3"] == -175.0

    txs = mgr.simplify_debts()
    # Simplified transactions: exactly 2 transactions instead of 3
    assert len(txs) == 2
    total_settled = sum(amt for _, _, amt in txs)
    assert total_settled == 200.0

    print("✅ expense_sharing_splitwise tests passed successfully!")


if __name__ == "__main__":
    run_tests()
