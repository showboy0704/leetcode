class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        def binary(lo, hi, nums):
            mid = (lo+hi)//2
            if lo > hi:
                return lo
            if nums[mid] < nums[mid+1]:
                return binary(mid+1, hi, nums)
            else:
                return binary(lo, mid-1, nums)
        return binary(0, len(arr)-1, arr)


if __name__ == '__main__':
    arr = [3,9,8,6,4]
    print(f"{arr}")
    print('----------Answer Below----------')
    print(Solution().peakIndexInMountainArray(arr))
