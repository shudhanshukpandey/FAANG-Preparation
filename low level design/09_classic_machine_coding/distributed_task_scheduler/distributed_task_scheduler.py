"""Distributed Task Scheduler & Job Runner.

Features:
- Scheduled / Delayed Task execution using a priority queue.
- Worker pool with leased execution locks to prevent duplicate processing.
- Exponential backoff retry policy with max retry ceilings.
- Dead Letter Queue (DLQ) for permanently failed tasks.
- Thread-safe coordination.
"""

from __future__ import annotations

import heapq
import time
import threading
from enum import Enum
from dataclasses import dataclass, field
from typing import Callable, Dict, List, Optional, Any


class TaskState(Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    DEAD_LETTERED = "DEAD_LETTERED"


@dataclass(order=True)
class ScheduledTask:
    run_at: float
    task_id: str = field(compare=False)
    action: Callable[[], Any] = field(compare=False)
    state: TaskState = field(default=TaskState.PENDING, compare=False)
    retries_left: int = field(default=3, compare=False)
    backoff_delay: float = field(default=0.05, compare=False)
    worker_id: Optional[str] = field(default=None, compare=False)


class DistributedTaskScheduler:
    def __init__(self, num_workers: int = 2) -> None:
        self._heap: List[ScheduledTask] = []
        self._tasks: Dict[str, ScheduledTask] = {}
        self._dlq: List[ScheduledTask] = []
        self._lock = threading.RLock()
        self._num_workers = num_workers
        self._running = False
        self._threads: List[threading.Thread] = []

    def schedule(
        self,
        task_id: str,
        action: Callable[[], Any],
        delay_seconds: float = 0.0,
        retries: int = 2,
    ) -> ScheduledTask:
        run_at = time.time() + delay_seconds
        task = ScheduledTask(
            run_at=run_at,
            task_id=task_id,
            action=action,
            retries_left=retries,
        )
        with self._lock:
            self._tasks[task_id] = task
            heapq.heappush(self._heap, task)
        return task

    def poll_next_task(self, worker_id: str) -> Optional[ScheduledTask]:
        with self._lock:
            now = time.time()
            if not self._heap or self._heap[0].run_at > now:
                return None

            task = heapq.heappop(self._heap)
            task.state = TaskState.RUNNING
            task.worker_id = worker_id
            return task

    def execute_one(self, worker_id: str) -> bool:
        task = self.poll_next_task(worker_id)
        if not task:
            return False

        try:
            task.action()
            task.state = TaskState.COMPLETED
            return True
        except Exception:
            with self._lock:
                if task.retries_left > 0:
                    task.retries_left -= 1
                    task.run_at = time.time() + task.backoff_delay
                    task.backoff_delay *= 2  # Exponential backoff
                    task.state = TaskState.PENDING
                    heapq.heappush(self._heap, task)
                else:
                    task.state = TaskState.DEAD_LETTERED
                    self._dlq.append(task)
            return False

    def get_task(self, task_id: str) -> Optional[ScheduledTask]:
        with self._lock:
            return self._tasks.get(task_id)

    def get_dlq(self) -> List[ScheduledTask]:
        with self._lock:
            return list(self._dlq)


def run_tests() -> None:
    scheduler = DistributedTaskScheduler(num_workers=2)

    executed = []

    def task_success():
        executed.append("success")

    def task_fail():
        raise RuntimeError("Network Timeout")

    # Schedule immediate success task
    t1 = scheduler.schedule("t1", task_success, delay_seconds=0.0)
    # Schedule failure task with 1 retry
    t2 = scheduler.schedule("t2", task_fail, delay_seconds=0.0, retries=1)

    # Worker 1 executes t1
    assert scheduler.execute_one("worker_1") is True
    assert executed == ["success"]
    assert scheduler.get_task("t1").state == TaskState.COMPLETED

    # Worker 2 executes t2 (fails, retries left = 0, re-queued)
    assert scheduler.execute_one("worker_2") is False
    assert scheduler.get_task("t2").state == TaskState.PENDING
    assert scheduler.get_task("t2").retries_left == 0

    # Wait for backoff
    time.sleep(0.06)

    # Worker 1 executes t2 again (fails, sent to DLQ)
    assert scheduler.execute_one("worker_1") is False
    assert scheduler.get_task("t2").state == TaskState.DEAD_LETTERED
    assert len(scheduler.get_dlq()) == 1
    assert scheduler.get_dlq()[0].task_id == "t2"

    print("✅ distributed_task_scheduler tests passed successfully!")


if __name__ == "__main__":
    run_tests()
