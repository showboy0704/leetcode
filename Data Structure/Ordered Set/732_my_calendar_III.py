from collections import Counter


class MyCalendarThree:

    def __init__(self):
        self.table = Counter()

    def book(self, start: int, end: int) -> int:
        self.table[start] += 1
        self.table[end] -= 1
        cur_k = max_k = 0
        for _, k in sorted(self.table.items()):
            cur_k += k
            max_k = max(cur_k, max_k)
        return max_k
