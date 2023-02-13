class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        pascal = [1, 1]
        for _ in range(2, n):
            pre_pascal = pascal
            pascal = []
            for j in range(len(pre_pascal)-1):
                pascal.append(pre_pascal[j]+pre_pascal[j+1])
            pascal = [1]+pascal+[1]
        return sum([pascal[i]*nums[i] for i in range(n)]) % 10


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    print(f"{nums}")
    print('----------Answer Below----------')
    print(Solution().triangularSum(nums))
