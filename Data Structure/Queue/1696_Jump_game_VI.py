from collections import deque


class Solution:
    def maxResult(self, nums: list[int], k: int) -> int:
        n = len(nums)
        queue = deque([0])
        for i in range(1, n):
            nums[i] = nums[queue[0]] + nums[i]
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
            if i - queue[0] >= k:
                queue.popleft()
        return nums[n - 1]


if __name__ == '__main__':
    nums, k = [10,-5,-2,4,0,3], 3
    print(f"{ nums,k}")
    print('----------Answer Below----------')
    print(Solution().maxResult(nums, k))
