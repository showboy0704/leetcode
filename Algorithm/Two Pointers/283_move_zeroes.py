class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        n = len(nums)
        i = 0
        for j in range(n):
            if nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            elif nums[i] != 0:
                i += 1

if __name__ == '__main__':
    nums = [1, 1, 0, 3, 12]
    print(f"{nums}")
    print('----------Answer Below----------')
    print(Solution().moveZeroes(nums))
