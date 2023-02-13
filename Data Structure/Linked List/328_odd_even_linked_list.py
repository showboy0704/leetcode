# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd_dumb_head = ListNode()
        evn_dumb_head = ListNode()
        odd_head = odd_dumb_head
        evn_head = evn_dumb_head
        i = 1
        while head is not None:
            if i % 2 == 1:
                odd_head.next = head
                odd_head = odd_head.next
            else:
                evn_head.next = head
                evn_head = evn_head.next
            head = head.next
            i+=1

        if i % 2 == 0:
            evn_head.next = head
            evn_head = evn_head.next

        odd_head.next = evn_dumb_head.next
        return odd_dumb_head.next
