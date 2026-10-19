"""Iterator Pattern: Transparent, memory-efficient paginated database cursor."""

from typing import Iterator, List


class User:
    def __init__(self, user_id: int, name: str) -> None:
        self.user_id = user_id
        self.name = name

    def __repr__(self) -> str:
        return f"User(id={self.user_id}, name={self.name!r})"


# Simulates a remote Database table with 10 records
MOCK_REMOTE_DB = [User(i, f"User_{i}") for i in range(1, 11)]


class PaginatedDatabaseCursor:
    """Custom Iterator that lazily fetches records from a database page by page."""

    def __init__(self, page_size: int = 3) -> None:
        self.page_size = page_size
        self._current_page = 0
        self._buffer: List[User] = []
        self._buffer_index = 0
        self._total_fetched = 0

    def __iter__(self) -> Iterator[User]:
        return self

    def _fetch_next_page(self) -> bool:
        start = self._current_page * self.page_size
        end = start + self.page_size
        records = MOCK_REMOTE_DB[start:end]

        if not records:
            return False  # No more data in DB

        print(f"\n  [DB I/O] Fetched page {self._current_page + 1} ({len(records)} records from index {start}..{end})")
        self._buffer = records
        self._buffer_index = 0
        self._current_page += 1
        return True

    def __next__(self) -> User:
        # If current buffer is exhausted, fetch next page from DB
        if self._buffer_index >= len(self._buffer):
            has_more = self._fetch_next_page()
            if not has_more:
                raise StopIteration

        item = self._buffer[self._buffer_index]
        self._buffer_index += 1
        return item


if __name__ == "__main__":
    cursor = PaginatedDatabaseCursor(page_size=4)

    print("Iterating over paginated cursor transparently:")
    for user in cursor:
        print(f" -> Processed: {user}")
