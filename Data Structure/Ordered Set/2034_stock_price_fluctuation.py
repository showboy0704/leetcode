from heapq import heappush, heappop


class StockPrice:

    def __init__(self):
        self.timestamps = {}
        self.curr = 0
        self.min_heap,self.max_heap = [],[]

    def update(self, timestamp: int, price: int) -> None:
        self.timestamps[timestamp] = price
        self.curr = max(self.curr, timestamp)

        heappush(self.min_heap, (price, timestamp))
        heappush(self.max_heap, (-price, timestamp))

    def current(self) -> int:
        return self.timestamps[self.curr]

    def maximum(self) -> int:
        price, timestamp = heappop(self.max_heap)

        while -price != self.timestamps[timestamp]:
            price, timestamp = heappop(self.max_heap)

        heappush(self.max_heap, (price, timestamp))
        return -price

    def minimum(self) -> int:
        price, timestamp = heappop(self.min_heap)

        while price != self.timestamps[timestamp]:
            price, timestamp = heappop(self.min_heap)

        heappush(self.min_heap, (price, timestamp))
        return price
