# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge(n1: ListNode, n2: ListNode) -> ListNode:
    head = ListNode()
    tail = head
    while n1 and n2:
        if n1.val < n2.val:
            tail.next = n1
            n1 = n1.next
        else:
            tail.next = n2
            n2 = n2.next
        tail = tail.next
    if n1:
        tail.next = n1
    if n2:
        tail.next = n2
    return head.next


class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        if not lists:
            return None
        if lists:
            k = len(lists)
            if k == 1:
                return lists[0]
            else:
                node = lists.pop()
                for i in range(k-1):
                    _node = lists.pop()
                    node = merge(node, _node)
                return node
