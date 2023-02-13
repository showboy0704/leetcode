import random

class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        def mth_small(nums, m):
            start, end = 0, len(nums)-1
            while True:
                pivot = nums[random.randint(start, end)]
                i, j, k = start, end, start
                while k <= j:
                    if nums[k] < pivot:
                        nums[i], nums[k] = nums[k], nums[i]
                        i += 1
                        k += 1
                    elif nums[k] > pivot:
                        nums[j], nums[k] = nums[k], nums[j]
                        j -= 1
                    else:
                        k += 1
                if i <= m-1 <= j:
                    return pivot
                elif m-1 < i:
                    end = i-1
                else:
                    start = i+1
        n = len(nums)
        mid = mth_small(nums, (n+1)//2)
        def mapIdx(i):
            return (1+2*i) % (n | 1)
        i, j, k = 0, n-1, 0
        while k <= j:
            if nums[mapIdx(k)] > mid:
                nums[mapIdx(k)], nums[mapIdx(i)] = nums[mapIdx(i)], nums[mapIdx(k)]
                i += 1
                k += 1
            elif nums[mapIdx(k)] < mid:
                nums[mapIdx(k)], nums[mapIdx(
                    j)] = nums[mapIdx(j)], nums[mapIdx(k)]
                j -= 1
            else:
                k += 1

        print(nums)
if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"{nums}")
    print('----------Answer Below----------')
    print(Solution().wiggleSort(nums))
