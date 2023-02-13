class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        lens = [1]*n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and lens[i] < lens[j]+1:
                    lens[i] = lens[j]+1
        return max(lens)

if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(f"{nums}")
    print('----------Answer Below----------')
    print(Solution().lengthOfLIS(nums))
