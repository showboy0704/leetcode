class Solution:
    def arraySign(self, nums: list[int]) -> int:
        if nums[0] == 0:
            return 0
        product = nums[0]//abs(nums[0])
        for num in nums[1:]:
            if num == 0:
                return 0
            else:
                product *= num//abs(num)
        return product


if __name__ == '__main__':
    nums = [-1, -2, -3, -4, 3, 2, 1]
    print(f"{nums}")
    print(Solution().arraySign(nums))
