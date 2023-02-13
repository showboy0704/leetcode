from collections import deque


class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        maxd, mind = deque(), deque()
        i = 0
        for num in nums:
            while maxd and num > maxd[-1]:
                maxd.pop()
            while mind and num < mind[-1]:
                mind.pop()
            maxd.append(num)
            mind.append(num)
            if maxd[0] - mind[0] > limit:
                if maxd[0] == nums[i]:
                    maxd.popleft()
                if mind[0] == nums[i]:
                    mind.popleft()
                i += 1
        return len(nums) - i


if __name__ == '__main__':
    nums = [10, 1, 2, 4, 7, 2]
    limit = 5
    print(f"{nums,limit}")
    print('----------Answer Below----------')
    print(Solution().longestSubarray(nums, limit))
