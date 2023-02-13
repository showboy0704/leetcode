class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        def binary(lo, hi, nums):
            if lo > hi:
                return -1
            mid = (lo+hi)//2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid-1
            elif nums[mid] < nums[mid+1]:
                return binary(mid+1, hi, nums)
            else:
                return binary(lo, mid-1, nums)
        nums = [-float('inf')]+nums+[-float('inf')]
        return binary(0, len(nums)-1, nums)


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print(f"{nums}")
    print('----------Answer Below----------')
    print(Solution().findPeakElement(nums))
