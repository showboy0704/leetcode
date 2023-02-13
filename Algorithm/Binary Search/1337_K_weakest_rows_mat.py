import heapq


class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        def binary(lo, hi, nums):
            if lo > hi:
                return lo
            mid = (lo+hi)//2
            if nums[mid] > 0:
                return binary(mid+1, hi, nums)
            else:
                return binary(lo, mid-1, nums)
        heap = []
        for i in range(len(mat)):
            soldiers = binary(0, len(mat[i])-1, mat[i])
            heapq.heappush(heap, (soldiers, i))
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result


if __name__ == '__main__':
    mat, k = [[1, 1, 0, 0, 0],
              [1, 1, 1, 1, 0],
              [1, 0, 0, 0, 0],
              [1, 1, 0, 0, 0],
              [1, 1, 1, 1, 1]], 3
print(f"{mat, k}")
print('----------Answer Below----------')
print(Solution().kWeakestRows(mat, k))
