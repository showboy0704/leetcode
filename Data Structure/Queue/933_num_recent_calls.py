class RecentCounter:

    def __init__(self):
        self.reqs = []

    def ping(self, t: int) -> int:
        self.reqs.append(t)
        n = len(self.reqs)
        count = pop_left = 0
        for i in range(n):
            req = self.reqs[i]
            if t-3000 <= req <= t:
                count += 1
            else:
                pop_left += 1
        self.reqs = self.reqs[pop_left:]
        return count


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
obj.ping(1)
obj.ping(100)
obj.ping(3001)
obj.ping(3002)
