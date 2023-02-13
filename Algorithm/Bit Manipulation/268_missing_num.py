class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        missing = 0
        for i in range(1, len(nums)+1):
            missing ^= i ^ nums[i-1]
        return missing


if __name__ == '__main__':
    nums = [0, 1]
    print(f"{nums}")
    print('----------Answer Below----------')
    print(Solution().missingNumber(nums))
