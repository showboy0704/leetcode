class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        if len(nums)<3:
            return True
        increase=None
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]>0:
                if increase is not None and not increase: 
                    return False
                increase=True
            if nums[i]-nums[i-1]<0:
                if increase is not None and increase: 
                    return False
                increase = False
        return True





if __name__ == '__main__':
    nums = [1,2,2,3]
    print(f"{nums}")
    print('----------Answer Below----------')
    print(Solution().isMonotonic(nums))
