class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i, n = 0, len(nums)
        for j in range(1, n):
            if nums[i] != nums[j]:
                nums[i+1], nums[j] = nums[j], nums[i+1]
                i += 1

        return nums


if __name__ == '__main__':
    nums = [1,1,2]
    print(f"{nums}")
    print('----------Answer Below----------')
    print(Solution().removeDuplicates(nums))
