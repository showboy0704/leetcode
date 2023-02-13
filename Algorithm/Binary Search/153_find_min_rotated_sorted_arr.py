class Solution:
    def findMin(self, nums: list[int]) -> int:
        def binary(lo, hi, nums):
            mid = (lo+hi) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] <= nums[0]:
                return binary(lo, mid-1, nums)
            else:
                return binary(mid+1, hi, nums)
        if len(nums) == 1:
            return nums[0]
        lo, hi = 0, len(nums)-1
        if nums[lo] < nums[hi]:
            return nums[lo]
        return binary(lo, hi, nums)


if __name__ == '__main__':
    nums = [5, 1, 2, 3, 4]
    print(f"{nums}")
    print('----------Answer Below----------')
    print(Solution().findMin(nums))
