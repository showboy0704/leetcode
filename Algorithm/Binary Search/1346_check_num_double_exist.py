class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        def binary(lo, hi, nums, target):
            if lo > hi:
                return None
            mid = (lo+hi)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary(mid+1, hi, nums, target)
            else:
                return binary(lo, mid-1, nums, target)
        arr.sort()
        for i in range(len(arr)):
            j = binary(0, len(arr)-1, arr, 2*arr[i])
            if j is not None and i != j:
                return True
        return False


if __name__ == '__main__':
    arr = [-2, 0, 10, -19, 4, 6, -8]
    print(f"{arr}")
    print('----------Answer Below----------')
    print(Solution().checkIfExist(arr))
