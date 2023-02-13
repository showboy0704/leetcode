# Definition for singly-linked list.
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: ListNode) -> int:
        max_sum = 0
        dq = deque()
        while head:
            dq.append(head.val)
            head = head.next
        while dq:
            max_sum = max(max_sum, dq.popleft()+dq.pop())
        return max_sum
