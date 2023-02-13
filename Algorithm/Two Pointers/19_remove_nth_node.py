class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: list[ListNode], n: int) -> list[ListNode]:
        length = 1
        first=head
        while first.next is not None:
            length+=1
            first=first.next
        if n == length:
            return head.next

        tagrget_node=head
        for _ in range(length-n-1):
            tagrget_node=tagrget_node.next
        tagrget_node.next=tagrget_node.next.next
        return head

