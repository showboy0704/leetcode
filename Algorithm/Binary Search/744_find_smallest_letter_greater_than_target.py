class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        def binary(lo, hi, nums, target):
            if lo > hi:
                if lo >= len(nums):
                    return nums[0]
                return nums[lo]
            mid = (lo+hi)//2
            if nums[mid] > target:
                return binary(lo, mid-1, nums, target)
            else:
                return binary(mid+1, hi, nums, target)
        return binary(0, len(letters)-1, letters, target)


if __name__ == '__main__':
    letter, targets = ["x", "x", "y", "y"], "z"
    print(f"{letter, targets}")
    print('----------Answer Below----------')
    print(Solution().nextGreatestLetter(letter, targets))
