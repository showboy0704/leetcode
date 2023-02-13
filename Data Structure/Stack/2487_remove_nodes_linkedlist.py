# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: ListNode) -> ListNode:
        stack = []
        while head:
            while stack and head.val > stack[-1].val:
                stack.pop()
            if stack:
                stack[-1].next = head
            stack.append(head)
            head = head.next
        return stack[0]
