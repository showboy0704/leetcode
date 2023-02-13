class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        def binary(lo, hi, arr, k):
            if lo > hi:
                return lo+k
            mid = (lo+hi)//2
            if arr[mid]-1-mid < k:
                return binary(mid+1, hi, arr, k)
            else:
                return binary(lo, mid-1, arr, k)
        return binary(0, len(arr)-1, arr, k)


if __name__ == '__main__':
    arr, k = [2, 3, 4, 7, 11], 5
    print(f"{arr, k}")
    print('----------Answer Below----------')
    print(Solution().findKthPositive(arr, k))
