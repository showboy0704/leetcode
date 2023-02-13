class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        tailA, tailB = headA, headB
        while tailA is not tailB:
            tailA = headB if tailA is None else tailA.next
            tailB = headA if tailB is None else tailB.next
        return tailA
