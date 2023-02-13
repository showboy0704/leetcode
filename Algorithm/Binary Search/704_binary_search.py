class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def binary(lo, hi, nums, target):
            if lo > hi:
                return -1
            mid = (lo+hi)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary(mid+1, hi, nums, target)
            else:
                return binary(lo, mid-1, nums, target)
        return binary(0, len(nums)-1, nums, target)


if __name__ == '__main__':
    nums, target = [5], 5
    print(f"{nums,target}")
    print('----------Answer Below----------')
    print(Solution().search(nums, target))
