class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        def binary(lo, hi, nums):
            if lo > hi:
                if -1 <= lo < len(nums) and nums[lo] <= -1:
                    return lo
                return -1
            mid = (lo+hi)//2
            if nums[mid] > -1:
                return binary(mid+1, hi, nums)
            else:
                return binary(lo, mid-1, nums)
        count = 0
        for nums in grid:
            index = binary(0, len(grid[0])-1, nums)
            if index != -1:
                count += len(grid[0])-index
        return count


if __name__ == '__main__':
    grid = [[5,1,0],[-5,-5,-5]]
    print(f"{grid}")
    print('----------Answer Below----------')
    print(Solution().countNegatives(grid))
