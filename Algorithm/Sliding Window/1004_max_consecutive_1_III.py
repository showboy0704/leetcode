class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l, r, n = 0, 0, len(nums)
        total = 0
        while r < n:
            total += nums[r]
            if total+k < r-l+1:
                total -= nums[l]
                l += 1
            r += 1
        return r-l


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    k = 3
    print(f"{nums,k}")
    print('----------Answer Below----------')
    print(Solution().longestOnes(nums, k))
