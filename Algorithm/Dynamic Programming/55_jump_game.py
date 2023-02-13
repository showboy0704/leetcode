class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        result, k = True, n-1
        for i in range(n-2, -1, -1):
            if i+nums[i] >= k:
                result, k = True, i
            else:
                result = False
        return result


if __name__ == '__main__':
    nums = [0, 2, 3]
    print(f"{nums}")
    print('----------Answer Below----------')
    print(Solution().canJump(nums))
