class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1, -1]

        def binary(lo, hi, nums, target, bound):
            mid = (lo+hi)//2
            if bound == 'hi':
                if lo > hi:
                    if 0 <= hi < len(nums):
                        return hi if nums[hi] == target else -1
                    else:
                        return -1
                if nums[mid] <= target:
                    return binary(mid+1, hi, nums, target, bound)
                else:
                    return binary(lo, mid-1, nums, target, bound)
            if bound == 'lo':
                if lo > hi:
                    if 0 <= lo < len(nums):
                        return lo if nums[lo] == target else -1
                    else:
                        return -1
                if nums[mid] < target:
                    return binary(mid+1, hi, nums, target, bound)
                else:
                    return binary(lo, mid-1, nums, target, bound)
        return [binary(0, len(nums)-1, nums, target, 'lo'), binary(0, len(nums)-1, nums, target, 'hi')]


if __name__ == '__main__':
    nums, target = [2, 2], 3
    print(f"{nums,target}")
    print('----------Answer Below----------')
    print(Solution().searchRange(nums, target))
