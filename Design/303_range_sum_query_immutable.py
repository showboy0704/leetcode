class NumArray:

    def __init__(self, nums: list[int]):
        self.prefix = [0]+nums
        for i in range(1, len(self.prefix)):
            self.prefix[i] += self.prefix[i-1]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1]-self.prefix[left]
