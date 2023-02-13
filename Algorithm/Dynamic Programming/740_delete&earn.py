class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        memo = [0]*10000
        for num in nums:
            memo[num-1] += num
        memo[1] = max(memo[0], memo[1])
        for i in range(2, 10000):
            memo[i] = max(memo[i]+memo[i-2], memo[i-1])
        return memo[-1]


if __name__ == '__main__':
    nums = [4,10,10,8,1,1,1,2,4,10,9,7,6]
    print(f"{nums}")
    print('----------Answer Below----------')
    print(Solution().deleteAndEarn(nums))
