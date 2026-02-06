# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. 
# Otherwise, add the key-value pair to the cache. 
# If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.used = deque()
        self.cache = {}
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.use(key)
        return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache and len(self.cache) >= self.capacity:
            lru = self.used.popleft()
            self.cache.pop(lru)
        self.use(key)
        self.cache[key] = value

    
    def use(self, key):
        if key in self.used:
            self.used.remove(key)
        self.used.append(key)
        


# Your LRUCache object will be instantiated and called as such:
capacity = 2
obj = LRUCache(capacity)

print(
    obj.put(1,1),
    obj.put(2,2),
    obj.get(1),
    obj.put(3,3),
    obj.get(2)
)