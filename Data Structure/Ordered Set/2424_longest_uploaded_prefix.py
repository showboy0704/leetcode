class LUPrefix:

    def __init__(self, n: int):
        self.order, self.prefix = [1]+[0]*n, 0

    def upload(self, video: int) -> None:
        if self.order[video] == 0:
            self.order[video] = 1
            for i in range(self.prefix, len(self.order)):
                if self.order[i] == 1:
                    self.prefix = i
                else:
                    return

    def longest(self) -> int:
        return self.prefix
