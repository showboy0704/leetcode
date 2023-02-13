class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        subsets, n = [], len(nums)
        nth_bit = 1 << n
        for i in range(2**n):
            bit_mask = bin(i | nth_bit)[3:]
            subset = []
            for i, bit in enumerate(bit_mask):
                print(bit)
                if int(bit) == 1:
                    subset.append(nums[i])
            subsets.append(subset)
        return subsets


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(f"{nums}")
    print(Solution().subsets(nums))
