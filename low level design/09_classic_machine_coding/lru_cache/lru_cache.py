"""LRU Cache: O(1) Get and Put using Hash Map + Doubly Linked List."""

from typing import Dict, Optional, Any


class Node:
    def __init__(self, key: str, val: Any) -> None:
        self.key = key
        self.val = val
        self.prev: Optional["Node"] = None
        self.next: Optional["Node"] = None


class LRUCache:
    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("Capacity must be positive.")
        self.capacity = capacity
        self.map: Dict[str, Node] = {}

        # Sentinel dummy head and tail nodes
        self.head = Node("HEAD_SENTINEL", None)
        self.tail = Node("TAIL_SENTINEL", None)
        self.head.next = self.tail
        self.tail.prev = self.head

    # Helper: Remove a node from doubly linked list in O(1)
    def _remove(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next
        if prev_node and next_node:
            prev_node.next = next_node
            next_node.prev = prev_node

    # Helper: Insert node right after Head (Most Recently Used) in O(1)
    def _insert_at_head(self, node: Node) -> None:
        node.next = self.head.next
        node.prev = self.head
        if self.head.next:
            self.head.next.prev = node
        self.head.next = node

    def get(self, key: str) -> Optional[Any]:
        if key not in self.map:
            return None
        node = self.map[key]
        # Move accessed node to head (MRU)
        self._remove(node)
        self._insert_at_head(node)
        return node.val

    def put(self, key: str, val: Any) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = val
            self._remove(node)
            self._insert_at_head(node)
        else:
            if len(self.map) >= self.capacity:
                # Evict least recently used (node right before tail)
                lru_node = self.tail.prev
                if lru_node and lru_node != self.head:
                    self._remove(lru_node)
                    del self.map[lru_node.key]
                    print(f"  [LRUCache Eviction] Evicted least recently used key: '{lru_node.key}'")

            new_node = Node(key, val)
            self._insert_at_head(new_node)
            self.map[key] = new_node

    def display_state(self) -> None:
        items = []
        curr = self.head.next
        while curr and curr != self.tail:
            items.append(f"({curr.key}: {curr.val})")
            curr = curr.next
        print(f"Current Cache Order (MRU -> LRU): {' <-> '.join(items)}")


if __name__ == "__main__":
    cache = LRUCache(capacity=3)

    print("Putting A=1, B=2, C=3:")
    cache.put("A", 1)
    cache.put("B", 2)
    cache.put("C", 3)
    cache.display_state()

    print("\nAccessing key 'A' (should become Most Recently Used):")
    val_a = cache.get("A")
    print(f"get('A') = {val_a}")
    cache.display_state()

    print("\nPutting key 'D'=4 (Exceeds capacity 3 -> should evict 'B'):")
    cache.put("D", 4)
    cache.display_state()

    print(f"Is 'B' evicted? {cache.get('B') is None}")  # True
