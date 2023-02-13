class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Boyer-Moore Voting Algorithm
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate


if __name__ == '__main__':
    nums = [3, 2, 3]
    print(f"{nums }")
    print('----------Answer Below----------')
    print(Solution().majorityElement(nums))
