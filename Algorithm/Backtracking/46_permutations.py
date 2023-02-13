class Solution:
    def backtrack(self, dim: int):
        if dim == len(self.nums):
            self.results.append(self.result[:])
            return

        for num in self.nums:
            if num not in self.result:
                self.result[dim] = num
                self.backtrack(dim+1)
                self.result[dim]=None


    def permute(self, nums: list[int]) -> list[list[int]]:
        self.result = [None] * len(nums)
        self.nums = nums
        self.results = []
        if nums:
            self.backtrack(0)
        return self.results


if __name__ == '__main__':
    nums = [1,2,3]
    print(f"{nums}")
    print('----------Answer Below----------')
    print(Solution().permute(nums))
