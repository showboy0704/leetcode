class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n, _nums = len(nums), nums[::-1]
        for i in range(1, n):
            nums[i] *= nums[i-1] or 1
            _nums[i] *= _nums[i-1] or 1
        return max(nums+_nums)


if __name__ == '__main__':
    nums = [-2,8,8,0]
    print(f"{nums}")
    print('----------Answer Below----------')
    print(Solution().maxProduct(nums))
