class Solution:
    def getMaxLen(self, nums: list[int]) -> int:
        n = len(nums)
        cur_pos = cur_neg = 0
        if nums[0] > 0:
            cur_pos = 1
        if nums[0] < 0:
            cur_neg = 1
        ans = cur_pos
        for i in range(1, n):
            if nums[i] > 0:
                cur_pos = 1 + cur_pos
                cur_neg = 1 + cur_neg if cur_neg > 0 else 0
            elif nums[i] < 0:
                cur_pos = 1 + cur_neg if cur_neg > 0 else 0
                cur_neg = 1 + cur_pos
            else:
                cur_pos = cur_neg = 0

            ans = max(ans, cur_pos)
        return ans


if __name__ == '__main__':
    nums = [0, 1, -2, -3, -4]
    print(f"{nums}")
    print('----------Answer Below----------')
    print(Solution().getMaxLen(nums))
