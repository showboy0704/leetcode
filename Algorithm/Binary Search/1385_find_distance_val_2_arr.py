class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        def binary(lo, hi, nums, target, d):
            if lo > hi:
                return 0
            mid = (lo+hi)//2
            if abs(nums[mid]-target) <= d:
                return 1
            elif nums[mid]-target < d:
                return binary(mid+1, hi, nums, target, d)
            else:
                return binary(lo, mid-1, nums, target, d)
        arr2.sort()
        num = len(arr1)
        for ele1 in arr1:
            num -= binary(0, len(arr2)-1, arr2, ele1, d)
            continue
        return num


if __name__ == '__main__':
    arr1, arr2, d = [4, 5, 8], [10, 9, 1, 8], 2
    print(f"{arr1, arr2 , d}")
    print('----------Answer Below----------')
    print(Solution().findTheDistanceValue(arr1, arr2, d))
