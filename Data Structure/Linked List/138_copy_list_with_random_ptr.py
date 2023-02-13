class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        if head is None:
            return None
        dummy_head = Node(0)
        old = head
        dummy_head.next = old
        while old is not None:
            val, next, random = old.val, old.next, old.random
            copy = Node(val, next, random)
            old.next = copy
            old = old.next.next

        new = dummy_head.next
        while new is not None and new.next is not None:
            copy_random = None if new.random is None else new.random.next
            new.next.random=copy_random
            new=new.next.next
        dummy_head.next=dummy_head.next.next
        new = dummy_head.next
        while new.next is not None:
            new.next = new.next.next
            new = new.next
        return dummy_head.next
