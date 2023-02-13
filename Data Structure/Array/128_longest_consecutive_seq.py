class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longest = 0
        num_set = set(nums)
        for n in num_set:
            if (n-1) not in num_set:
                length = 1
                while (n+length) in num_set:
                    length += 1
                longest = max(longest, length)
        return longest


if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]
    print(f"{nums}")
    print('----------Answer Below----------')
    print(Solution().longestConsecutive(nums))
