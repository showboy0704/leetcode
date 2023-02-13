class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums = sorted(nums)[::-1]
        for i in range(len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0


if __name__ == '__main__':
    nums = [2, 1, 2]
    print(f"{nums}")
    print(Solution().largestPerimeter(nums))
