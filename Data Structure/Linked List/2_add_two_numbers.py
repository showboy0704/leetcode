class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_list_item(self, item):

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item
        self.length += 1

    def to_int(self):
        result = 0
        power = 0
        item = self.head
        while item is not None:
            result += item.val*(10 ** power)
            power += 1
            item = item.next
        return result

    def __add__(self, other):
        result_l = []
        min_len = min(self.length, other.length)
        max_len = max(self.length, other.length)
        item_s, item_o, carry = self.head, other.head, 0
        for i in range(min_len):
            result = item_s.val+item_o.val + carry
            item_s, item_o, carry = item_s.next, item_o.next, 0
            if result > 9:
                carry = 1
                result = result % 10
            result_l.append(result)
        if self.length > other.length:
            longer = item_s
        else:
            longer = item_o
        if max_len != min_len:
            for i in range(max_len-min_len):
                result = longer.val + carry
                longer, carry = longer.next, 0
                if result > 9:
                    carry = 1
                    result = result % 10
                result_l.append(result)
        if carry > 0:
            result_l.append(1)
        return result_l


class Solution:
    def addTwoNumbers(self, l1: SingleLinkedList, l2: SingleLinkedList) -> SingleLinkedList:
        result_l = []
        carry = 0
        longer = None
        while l1 is not None and l2 is not None:
            result = l1.val+l2.val + carry
            l1, l2, carry = l1.next, l2.next, 0
            if result > 9:
                carry = 1
                result = result % 10
            result_l.append(result)
        if l1 is not None and l2 is None:
            longer = l1
        elif l2 is not None and l1 is None:
            longer = l2
        while longer is not None:
            result =longer.val + carry
            longer, carry = longer.next, 0
            if result > 9:
                carry = 1
                result = result % 10
            result_l.append(result)

        if carry > 0:
            result_l.append(1)
        sl1 = SingleLinkedList()
        for item in result_l:
            sl1.add_list_item(ListNode(item))
        return sl1.head

if __name__ == '__main__':
    l1 = [9, 9, 9, 9, 9, 9, 9]
    l2 = [9, 9, 9, 9]
    print(f"{l1}, {l2}")
    sl1, sl2 = SingleLinkedList(), SingleLinkedList()
    for item in l1:
        sl1.add_list_item(ListNode(item))
    for item in l2:
        sl2.add_list_item(ListNode(item))
    print(sl1+sl2)
    # print(Solution().addTwoNumbers(l1=sl1, l2=sl2))
