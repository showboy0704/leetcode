class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        table, stack = {}, []
        for num in nums2:
            while stack and num > stack[-1]:
                table[stack.pop()] = num

            table[num] = -1
            stack.append(num)
        result = []
        for num in nums1:
            result.append(table[num])
        return result


if __name__ == '__main__':
    nums1, nums2 = [4, 1, 2], [1, 3, 4, 2]
    print(f"{nums1 , nums2}")
    print(Solution().nextGreaterElement(nums1, nums2))
