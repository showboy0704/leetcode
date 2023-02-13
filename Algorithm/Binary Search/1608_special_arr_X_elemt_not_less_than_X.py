class Solution:
    def specialArray(self, nums: list[int]) -> int:
        def binary(lo, hi, nums, target):
            if lo > hi:
                return len(nums)-1-hi
            mid = (lo+hi)//2
            if nums[mid] < target:
                return binary(mid+1, hi, nums, target)
            else:
                return binary(lo, mid-1, nums, target)
        nums.sort()
        for i in range(1, len(nums)+1):
            if i == binary(0, len(nums)-1, nums, i):
                return i
        return -1


if __name__ == '__main__':
    nums = [3, 5]
    print(f"{nums}")
    print('----------Answer Below----------')
    print(Solution().specialArray(nums))
