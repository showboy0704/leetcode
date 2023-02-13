class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        def binary(lo, hi, nums, target):
            if lo > hi:
                return False
            mid = (lo+hi)//2
            if nums[mid] == target:
                del nums[mid]
                return True
            elif nums[mid] < target:
                return binary(mid+1, hi, nums, target)
            else:
                return binary(lo, mid-1, nums, target)
        intersection = []
        longer = nums1 if len(nums1) >= len(nums2) else nums2
        shorter = nums2 if len(nums2) <= len(nums1) else nums1
        longer.sort()
        for num in shorter:
            if binary(0, len(longer)-1, longer, num):
                intersection.append(num)
        return intersection


if __name__ == '__main__':
    nums1, nums2 = [1, 2, 2, 1], [2, 2, 2, 2]
    print(f"{nums1 , nums2}")
    print('----------Answer Below----------')
    print(Solution().intersect(nums1, nums2))
