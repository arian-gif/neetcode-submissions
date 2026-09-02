class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.nxt = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)      # dummy: most-recent side
        self.tail = Node(0, 0)      # dummy: least-recent side
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.nxt = node.nxt    # never None: real nodes always sit between dummies
        node.nxt.prev = node.prev

    def _add_front(self, node):     # front = right after head = most recent
        first = self.head.nxt
        node.prev = self.head
        node.nxt = first
        self.head.nxt = node
        first.prev = node

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)          # detach from wherever
        self._add_front(node)       # re-add as most recent
        return node.value

    def put(self, key, value):
        if key in self.cache:       # Bug 5 fix: remove old node first
            self._remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self._add_front(node)
        if len(self.cache) > self.capacity:
            lru = self.tail.prev    # least-recent real node
            self._remove(lru)
            del self.cache[lru.key]