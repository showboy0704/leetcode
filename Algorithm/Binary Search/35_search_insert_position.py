class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        def binary(start, end, nums, target):
            if start > end:
                return (start+end)//2+1
            mid = (start+end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary(mid+1, end, nums, target)
            else:
                return binary(start, mid-1, nums, target)
        return binary(0, len(nums)-1, nums, target)


if __name__ == '__main__':
    nums, target = [1, 3, 5, 7], 4
    print(f"{nums,target}")
    print('----------Answer Below----------')
    print(Solution().searchInsert(nums, target))
