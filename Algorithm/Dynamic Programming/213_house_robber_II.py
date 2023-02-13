class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[1], nums[0])
        rob_l, not_rob_l = nums[0], max(nums[1], nums[0])
        rob_r, not_rob_r = nums[1], max(nums[2], nums[1])
        for i in range(2, len(nums)-1):
            rob_l, not_rob_l = not_rob_l, max(nums[i]+rob_l, not_rob_l)
            rob_r, not_rob_r = not_rob_r, max(nums[i+1]+rob_r, not_rob_r)
        return max(not_rob_l, not_rob_r)


if __name__ == '__main__':
    nums = [1, 3, 1, 3, 100]
    print(f"{nums}")
    print('----------Answer Below----------')
    print(Solution().rob(nums))
