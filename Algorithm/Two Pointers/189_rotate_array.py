class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = (nums+nums)[len(nums)-k:(2*len(nums))-k]
        print(nums)


if __name__ == '__main__':
    nums = [-1,2]
    k = 2
    print(f"{nums}")
    print('----------Answer Below----------')
    print(Solution().rotate(nums,k))
    print(nums)
