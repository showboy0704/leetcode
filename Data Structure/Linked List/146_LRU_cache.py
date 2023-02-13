class Node:
    def __init__(self, key: int, val: int, prev: 'Node' = None, next: 'Node' = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

    def __repr__(self) -> str:
        return f"key:{self.key},val:{self.val}"


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table  = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.table:
            node = self.table[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
            if key in self.table:
                self._remove(self.table[key])
            node = Node(key, value)
            self._add(node)
            self.table[key] = node
            if len(self.table) > self.capacity:
                node = self.head.next
                self._remove(node)
                del self.table[node.key]
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail


if __name__ == '__main__':
    obj = LRUCache(1)
    obj.put(2, 1)
    print(obj.get(1))
    obj.put(3, 3)
    param_1 = obj.get(2)
