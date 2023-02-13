class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    tail = ListNode()
    next_sublist = ListNode()

    def split(self, node: ListNode, size: int):
        mid_prev = node
        end = node.next
        for _ in range(1,size):
            if mid_prev.next is not None or end.next is not None:
                if end.next is not None:
                    end = end.next.next  if end.next.next is not None else end.next
                if mid_prev.next is not None:
                    mid_prev = mid_prev.next
        mid = mid_prev.next
        mid_prev.next = None
        self.next_sublist = end.next
        end.next = None
        return mid

    def merge(self, list1: ListNode, list2: ListNode):
        dummy_head = ListNode()
        new_tail = dummy_head
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                new_tail.next = list1
                list1 = list1.next
                new_tail = new_tail.next
            else:
                new_tail.next = list2
                list2 = list2.next
                new_tail = new_tail.next
        new_tail.next = list1 if list1 is not None else list2
        while new_tail.next is not None:
            new_tail = new_tail.next

        self.tail.next = dummy_head.next
        self.tail = new_tail

    def get_length(self,node: ListNode):
        length = 0
        pointer = node
        while pointer is not None:
            pointer = pointer.next
            length += 1
        return length

    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        length = self.get_length(head)
        start = head
        dummy_head = ListNode()
        for power in range(17):
            size = 2**power
            if size < length:
                self.tail = dummy_head
                while start is not None:
                    if start.next is None:
                        self.tail.next = start
                        break
                    mid = self.split(start, size)
                    self.merge(start, mid)
                    start = self.next_sublist
                start = dummy_head.next
        return dummy_head.next
