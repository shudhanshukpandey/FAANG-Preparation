"""Unit of Work (UoW) Pattern: Atomic multi-repository transactions via Python context managers."""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional
import uuid


# -------------------------------------------------------------
# 1. Domain Entities
# -------------------------------------------------------------
class Account:
    def __init__(self, acc_id: str, balance: float) -> None:
        self.acc_id = acc_id
        self.balance = balance

    def __repr__(self) -> str:
        return f"Account({self.acc_id}: ${self.balance:.2f})"


class AuditLog:
    def __init__(self, log_id: str, message: str) -> None:
        self.log_id = log_id
        self.message = message

    def __repr__(self) -> str:
        return f"AuditLog({self.log_id}: {self.message})"


# -------------------------------------------------------------
# 2. Repository Interfaces
# -------------------------------------------------------------
class AccountRepository(ABC):
    @abstractmethod
    def get(self, acc_id: str) -> Optional[Account]:
        pass

    @abstractmethod
    def update(self, account: Account) -> None:
        pass


class AuditLogRepository(ABC):
    @abstractmethod
    def add(self, log: AuditLog) -> None:
        pass


# -------------------------------------------------------------
# 3. Transaction-Aware Concrete Repositories
# -------------------------------------------------------------
class MemoryAccountRepository(AccountRepository):
    def __init__(self, staged_accounts: Dict[str, Account]) -> None:
        self._staged = staged_accounts

    def get(self, acc_id: str) -> Optional[Account]:
        acc = self._staged.get(acc_id)
        if not acc:
            return None
        # Return a copy to protect staged state until explicit update
        return Account(acc.acc_id, acc.balance)

    def update(self, account: Account) -> None:
        self._staged[account.acc_id] = account


class MemoryAuditLogRepository(AuditLogRepository):
    def __init__(self, staged_logs: List[AuditLog]) -> None:
        self._staged = staged_logs

    def add(self, log: AuditLog) -> None:
        self._staged.append(log)


# -------------------------------------------------------------
# 4. Abstract Unit of Work
# -------------------------------------------------------------
class AbstractUnitOfWork(ABC):
    accounts: AccountRepository
    audit_logs: AuditLogRepository

    def __enter__(self) -> "AbstractUnitOfWork":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        # Rollback by default if an exception occurred OR if commit() was never called
        if exc_type is not None or not getattr(self, "committed", False):
            self.rollback()

    @abstractmethod
    def commit(self) -> None:
        pass

    @abstractmethod
    def rollback(self) -> None:
        pass


# -------------------------------------------------------------
# 5. Concrete Unit of Work (In-Memory Transactional Simulation)
# -------------------------------------------------------------
class MemoryUnitOfWork(AbstractUnitOfWork):
    # Simulated persistent database tables
    COMMITTED_ACCOUNTS: Dict[str, float] = {"ACC_A": 500.0, "ACC_B": 100.0}
    COMMITTED_LOGS: List[str] = []

    def __init__(self) -> None:
        self.committed = False
        # Staged working copy for the transaction
        self._staged_accounts: Dict[str, Account] = {
            acc_id: Account(acc_id, bal) for acc_id, bal in self.COMMITTED_ACCOUNTS.items()
        }
        self._staged_logs: List[AuditLog] = []

        # Instantiate repositories bound to this UoW's staged transaction state
        self.accounts: AccountRepository = MemoryAccountRepository(self._staged_accounts)
        self.audit_logs: AuditLogRepository = MemoryAuditLogRepository(self._staged_logs)

    def __enter__(self) -> "MemoryUnitOfWork":
        print("[UoW] BEGIN TRANSACTION;")
        self.committed = False
        return self

    def commit(self) -> None:
        print("[UoW] COMMIT: Writing all staged changes atomically to persistent DB.")
        # Atomic commit to shared persistent state
        self.COMMITTED_ACCOUNTS.clear()
        for acc in self._staged_accounts.values():
            self.COMMITTED_ACCOUNTS[acc.acc_id] = acc.balance

        for log in self._staged_logs:
            self.COMMITTED_LOGS.append(f"{log.log_id}: {log.message}")

        self.committed = True

    def rollback(self) -> None:
        print("[UoW] ROLLBACK: Discarding staged changes! Database remains consistent.")
        self._staged_accounts.clear()
        self._staged_logs.clear()


# -------------------------------------------------------------
# 6. Service Layer Orchestration
# -------------------------------------------------------------
def execute_bank_transfer(uow: AbstractUnitOfWork, from_id: str, to_id: str, amount: float) -> None:
    """The service coordinates domain logic through the UoW's repositories."""
    with uow:
        sender = uow.accounts.get(from_id)
        receiver = uow.accounts.get(to_id)

        if not sender or not receiver:
            raise ValueError("Sender or Receiver account not found.")

        if sender.balance < amount:
            raise ValueError(f"Insufficient funds! {from_id} balance is ${sender.balance:.2f}, transfer requires ${amount:.2f}.")

        # Deduct and credit
        sender.balance -= amount
        receiver.balance += amount

        # Save to repositories
        uow.accounts.update(sender)
        uow.accounts.update(receiver)

        # Audit record
        log_id = f"LOG-{str(uuid.uuid4())[:6].upper()}"
        uow.audit_logs.add(AuditLog(log_id, f"Transferred ${amount:.2f} from {from_id} to {to_id}"))

        # Commit transaction
        uow.commit()


if __name__ == "__main__":
    print("Initial Persistent Balances:", MemoryUnitOfWork.COMMITTED_ACCOUNTS)

    # 1. Successful atomic transfer
    print("\n--- 1. Executing Valid Transfer ($150) ---")
    uow1 = MemoryUnitOfWork()
    execute_bank_transfer(uow1, "ACC_A", "ACC_B", 150.0)
    print("Updated Persistent Balances:", MemoryUnitOfWork.COMMITTED_ACCOUNTS)
    print("Committed Audit Logs:", MemoryUnitOfWork.COMMITTED_LOGS)

    # 2. Failed transfer with automatic rollback
    print("\n--- 2. Executing Overdrawn Transfer ($1,000) ---")
    uow2 = MemoryUnitOfWork()
    try:
        execute_bank_transfer(uow2, "ACC_A", "ACC_B", 1000.0)
    except ValueError as e:
        print(f"Caught expected error: {e}")

    print("Persistent Balances after failed attempt (unaltered!):", MemoryUnitOfWork.COMMITTED_ACCOUNTS)

    # 3. Uncommitted transaction (forgot commit / early exit -> auto-rollback)
    print("\n--- 3. Testing Uncommitted Context (Auto-Rollback by Default) ---")
    uow3 = MemoryUnitOfWork()
    with uow3:
        acc = uow3.accounts.get("ACC_A")
        if acc:
            acc.balance += 50000.0
            uow3.accounts.update(acc)
        # Notice: uow3.commit() is intentionally omitted!

    print("Persistent Balances after uncommitted block (safely unchanged):", MemoryUnitOfWork.COMMITTED_ACCOUNTS)
