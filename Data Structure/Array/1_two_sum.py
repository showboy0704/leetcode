class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_set = set(nums)
        for num in num_set:
            remain = target-num
            if remain in num_set:
                i = nums.index(num)
                j = nums.index(remain)
                if i != j:
                    return i, j
                else:
                    if nums.count(remain) > 1:
                        j = nums[i+1:].index(remain)+(i+1)
                        return i, j
    def twoSum_solution(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i

if __name__ == '__main__':
    nums = [2, 4, 11, 3]
    target = 6
    print(f"{nums}, {target}")
    print(Solution().twoSum_solution(nums=nums, target=target))
