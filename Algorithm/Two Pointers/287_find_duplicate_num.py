class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        tortoise, hare = nums[0], nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare


if __name__ == '__main__':
    nums = [1,3,4,2,2]
    print(f"{nums}")
    print('----------Answer Below----------')
    print(Solution().findDuplicate(nums))
