class Solution:
    def search(self, nums: list[int], target: int) -> int:
        i,steps = 0,0
        right,left = False,False
        while (not right or not left) and steps < len(nums):
            print(i)
            if target == nums[i]:
                if i < 0:
                    i += len(nums)
                return i
            elif target > nums[i]:
                i += 1
                right = True
            elif target < nums[i]:
                i -= 1
                left = True
            steps += 1
        if i < len(nums):
            if target == nums[i]:
                if i < 0:
                    i += len(nums)
                return i
        return -1


if __name__ == '__main__':
    nums = [1]
    target = 2
    print(f"{nums,target}")
    print('----------Answer Below----------')
    print(Solution().search(nums, target))
