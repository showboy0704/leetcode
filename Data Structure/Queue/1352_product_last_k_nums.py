class ProductOfNumbers:
    def __init__(self):
        self.queue = []

    def add(self, num: int) -> None:
        i = 0
        if num == 0:
            self.queue = []
        elif num != 1:
            while self.queue[i:]:
                self.queue[i] *= num
                i += 1
        self.queue.append(num)

    def getProduct(self, k: int) -> int:
        if k > len(self.queue):
            return 0
        return self.queue[-k]
