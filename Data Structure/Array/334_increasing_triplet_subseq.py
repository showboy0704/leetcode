class Solution:
    def increasingTriplet(self,nums):
        first = second = 2**31 - 1
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False


if __name__ == '__main__':
    nums = [1,5,0,4,1,3]
    print(f"{nums}")
    print('----------Answer Below----------')
    print(Solution().increasingTriplet(nums))
