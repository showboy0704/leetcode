class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result,result_set = [], []
        for i in range(len(nums)-2):
            j, k = i+1, len(nums)-1
            while j < k:
                if nums[i]+nums[j]+nums[k] == 0:
                    if set([nums[i], nums[j], nums[k]]) not in result_set:
                        result_set.append(set([nums[i], nums[j], nums[k]]))
                        result.append([nums[i], nums[j], nums[k]])
                    j = j+1
                if nums[i]+nums[j]+nums[k] > 0:
                    k = k-1
                if nums[i]+nums[j]+nums[k] < 0:
                    j = j+1
        return result


if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    print(f"{nums}")
    print('----------Answer Below----------')
    print(Solution().threeSum(nums))
