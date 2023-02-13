class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head, prev=None):
        # Iterative 
        '''        
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev
        '''
        # Recursive 
        if not head:
            return prev

        curr, head.next = head.next, prev
        return self.reverseList(curr, head)
