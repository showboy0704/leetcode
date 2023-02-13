class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        pre_product = [1]*n
        for i in range(1, n):
            pre_product[i] = pre_product[i-1]*nums[i-1]
        suf_product = [1]*n
        for i in range(n-2, -1, -1):
            suf_product[i] = suf_product[i+1]*nums[i+1]
        result = []
        for i in range(n):
            result.append(pre_product[i]*suf_product[i])

        return result


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(f"{nums}")
    print('----------Answer Below----------')
    print(Solution().productExceptSelf(nums))
