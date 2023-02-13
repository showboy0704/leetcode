class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        n = len(nums)
        max_sum, min_sum = nums[0], nums[0]
        cur_max, cur_min = 0, 0
        total = 0
        for i in range(n):
            cur_max = max(nums[i]+cur_max, nums[i])
            max_sum = max(cur_max, max_sum)
            cur_min = min(nums[i]+cur_min, nums[i])
            min_sum = min(cur_min, min_sum)
            total += nums[i]
        return max(max_sum, total-min_sum) if max_sum > 0 else max_sum


if __name__ == '__main__':
    nums = [1, -2, 3, -2]
    print(f"{ nums}")
    print('----------Answer Below----------')
    print(Solution().maxSubarraySumCircular(nums))
