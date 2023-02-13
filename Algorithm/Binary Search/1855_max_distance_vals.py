class Solution:
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        def binary(lo, hi, nums, target):
            if lo > hi:
                if len(nums) > hi >= 0:
                    return hi
                else:
                    return -1
            mid = (lo+hi)//2
            if nums[mid] >= target:
                return binary(mid+1, hi, nums, target)
            else:
                return binary(lo, mid-1, nums, target)
        max_d, m, n = 0, len(nums1), len(nums2)
        for i in range(m):
            j = binary(0, n-1, nums2, nums1[i])
            if j != -1:
                max_d = max(max_d, j-i)
        return max_d


if __name__ == '__main__':
    nums1, nums2 = [55, 30, 5, 4, 2], [100, 20, 10, 10, 5]
    print(f"{nums1 , nums2}")
    print('----------Answer Below----------')
    print(Solution().maxDistance(nums1, nums2))
