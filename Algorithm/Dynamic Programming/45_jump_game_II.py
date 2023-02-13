class Solution:
    def jump(self, nums: list[int]) -> int:
        answer, n = 0, len(nums)
        cur_end, cur_far = 0, 0
        for i in range(n - 1):
            cur_far = max(cur_far, i + nums[i])
            if i == cur_end:
                answer += 1
                cur_end = cur_far
        return answer


if __name__ == '__main__':
    nums = [1, 2, 1, 1, 1]
    print(f"{nums}")
    print('----------Answer Below----------')
    print(Solution().jump(nums))
