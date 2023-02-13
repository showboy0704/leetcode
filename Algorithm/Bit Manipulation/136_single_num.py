class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        single = 0
        for num in nums:
            single ^= num
        return single


if __name__ == '__main__':
    nums = [2, 2, 1]
    print(f"{nums}")
    print('----------Answer Below----------')
    print(Solution().singleNumber(nums))
