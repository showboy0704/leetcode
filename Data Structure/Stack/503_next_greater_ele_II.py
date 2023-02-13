class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result, stack = [-1]*n, []
        nums *= 2
        for i in range(2*n):
            while stack and nums[i] > nums[stack[-1]]:
                result[stack.pop() % n] = nums[i]
            stack.append(i)

        return result


if __name__ == '__main__':
    nums = [100, 1, 11, 1, 120, 111, 123, 1, -1, -100]
    print(f"{nums}")
    print(Solution().nextGreaterElements(nums))
