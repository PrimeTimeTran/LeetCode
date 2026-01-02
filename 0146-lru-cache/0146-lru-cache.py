class ListNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = ListNode(0,0), ListNode(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def insert(self, n) -> int:
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = n
        n.prev, n.next = prev, nxt

    def remove(self, n) -> int:
        prev, nxt = n.prev, n.next
        prev.next, nxt.prev = nxt, prev

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]