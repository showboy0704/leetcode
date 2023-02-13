class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        cur, tail = head, head.next
        while tail:
            if cur.val == tail.val:
                cur.next = tail.next

            else:
                cur = cur.next
            tail = cur.next
        return head
