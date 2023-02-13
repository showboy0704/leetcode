class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print(f"{nums }")
    print('----------Answer Below----------')
    print(Solution().containsDuplicate(nums))
