from collections import deque
class CacheEntry:
    def __init__(self,value,key):
        self.value =value
        self.key=key
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache=deque()
        self.keys={}

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        else:
            entry = self.keys[key]
            self.cache.remove(self.keys[key])
            self.cache.append(entry)
            return entry.value


    def put(self, key: int, value: int) -> None:
        if key not in self.keys:
            if len(self.cache)==self.capacity:
                delEntry=self.cache.popleft()
                self.keys.pop(delEntry.key)
                newEntry = CacheEntry(value,key)
                self.cache.append(newEntry)
                self.keys[key]=newEntry
            else:
                newCacheEntry = CacheEntry(value,key)
                self.cache.append(newCacheEntry)
                self.keys[key]=newCacheEntry
        else:
            entry = self.keys[key]
            self.cache.remove(entry)
            entry.value = value
            self.cache.append(entry)
