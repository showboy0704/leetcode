class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        d_head = tail = ListNode()
        while head:
            if head.val != val:
                tail.next = ListNode(head.val)
                tail = tail.next
            head = head.next

        return d_head.next
