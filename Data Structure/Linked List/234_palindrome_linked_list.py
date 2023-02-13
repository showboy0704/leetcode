class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def find_half(self, head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse(self, head):
        previous, current = None, head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous

    def isPalindrome(self, head: ListNode) -> bool:
        tail = self.reverse(self.find_half(head))

        while head and tail:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next

        return True
