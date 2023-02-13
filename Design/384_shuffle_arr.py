from random import randint
class Solution:

    def __init__(self, nums: list[int]):
        self.nums=nums

    def reset(self) -> list[int]:
        return self.nums

    def shuffle(self) -> list[int]:
        n = len(self.nums)
        shuffle=self.nums[:]
        for i in range(n):
            j = randint(i, n - 1)
            shuffle[i], shuffle[j] = shuffle[j], shuffle[i]
        return shuffle
