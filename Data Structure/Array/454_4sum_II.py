class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        count, table = 0, dict()
        for n in nums1:
            for m in nums2:
                if -(n+m) not in table:
                    table[-(n+m)] = 1
                else:
                    table[-(n+m)] += 1
        for n in nums3:
            for m in nums4:
                if n+m in table:
                    count += table[n+m]
        return count


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [-2, -1]
    nums3 = [-1, 2]
    nums4 = [0, 2]
    print(f"{nums1,nums2,nums3,nums4}")
    print('----------Answer Below----------')
    print(Solution().fourSumCount(nums1, nums2, nums3, nums4))
