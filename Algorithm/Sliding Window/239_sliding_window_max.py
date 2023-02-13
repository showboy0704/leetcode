from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        queue = deque()
        maxes = []
        for i in range(n):
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
            if queue[0] == i - k:
                queue.popleft()
            if i >= k - 1:
                maxes.append(nums[queue[0]])
        return maxes


if __name__ == '__main__':
    nums, k = [4, 10, 9, -7, -4, -8, 2, -6], 5
    print(f"{nums,k}")
    print('----------Answer Below----------')
    print(Solution().maxSlidingWindow(nums, k))
