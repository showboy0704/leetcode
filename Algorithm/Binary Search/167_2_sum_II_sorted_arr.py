class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
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
        for i in range(len(nums)):
            j = binary(i+1, len(nums)-1, nums, target-nums[i])
            if j != -1:
                return [i+1, j+1]


if __name__ == '__main__':
    numbers, target = [2, 7, 11, 15], 9
    print(f"{numbers,target}")
    print('----------Answer Below----------')
    print(Solution().twoSum(numbers, target))
