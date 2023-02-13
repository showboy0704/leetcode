class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        if n > 0:
            j = 0
            for i in range(m+n):
                if nums1[i] < nums2[j] and m-i+j < 1:
                    nums1[i] = nums2[j]
                    j += 1
                elif nums1[i] >= nums2[j]:
                    nums1[i+1:] = nums1[i:m+n-1]
                    nums1[i] = nums2[j]
                    j += 1
                if j > n-1:
                    break
            print(nums1)


if __name__ == '__main__':
    nums1 = [2, 0]
    m = 1
    nums2 = [1]
    n = 1
    print(f"{nums1, m,nums2,n}")
    print('----------Answer Below----------')
    print(Solution().merge(nums1, m, nums2, n))
