'''
1. Constraints
We'll receive a stream of data and we need to return values depending on the stream's messages.

2. Diagram

["LRUCache", "put",  "put",  "get", "put",  "get", "put",  "get", "get", "get"]
[[2],        [1, 1], [2, 2], [1],   [3, 3], [2],   [4, 4], [1],   [3],   [4]]
                                                                          ^                                                                          
CAP 2
CACHE

{
    3:3,
    4:4
}              

LL:
left > 3 > 4 > right

return 1
return -1
return -1
return 3
return 4

3. Pseudocode

We define a ListNode class which has keyy, value, next, and prev properties.
When we init LRUCache we define cap, cache, left, and right.

We define a get method which looks at our cache and updates it to the end of the linkedList if 

4. Code

'''

class ListNode:
    def __init__(self, key, val):
        self.key,self.val = key, val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left, self.right = ListNode(0,0), ListNode(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def remove(self, n) -> None:
        prev, nxt = n.prev, n.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, n) -> None:
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = n
        n.prev, n.next = prev, nxt

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]