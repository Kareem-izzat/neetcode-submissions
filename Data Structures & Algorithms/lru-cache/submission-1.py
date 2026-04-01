class CacheEntry:
    def __init__(self, value, key):
        self.value = value
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys = {}  
        self.head = CacheEntry(0, 0)  # Dummy head
        self.tail = CacheEntry(0, 0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _append(self, node):
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        entry = self.keys[key]
        self._remove(entry)
        self._append(entry)
        return entry.value

    def put(self, key: int, value: int) -> None:
        if key not in self.keys:
            if len(self.keys) == self.capacity:
                
                lru = self.head.next
                self._remove(lru)
                del self.keys[lru.key]
            
            newEntry = CacheEntry(value, key)
            self._append(newEntry)
            self.keys[key] = newEntry
        else:
            entry = self.keys[key]
            self._remove(entry)
            entry.value = value
            self._append(entry)
