class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max = nums[0]
        maxes = [max]
        for i in range(len(nums)-1):
            if max <= 0:
                max = nums[i+1]

            else:
                max += nums[i+1]

            if max > maxes[-1]:
                maxes.append(max)

        return maxes[-1]


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"{nums}")
    print('----------Answer Below----------')
    print(Solution().maxSubArray(nums))
