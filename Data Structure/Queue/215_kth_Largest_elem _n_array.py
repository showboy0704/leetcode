class Solution:
    def quick_select(self, left, right, k):
        if left > right:
            return
        i, j = left, right
        base = self.nums[left]
        while i != j:
            while self.nums[j] <= base and i < j:
                j -= 1
            while self.nums[i] >= base and i < j:
                i += 1
            if i < j:
                temp = self.nums[i]
                self.nums[i] = self.nums[j]
                self.nums[j] = temp
        self.nums[left] = self.nums[i]
        self.nums[i] = base
        if i == k-1:
            return self.nums[i]
        elif i > k-1:
            return self.quick_select(left, i-1, k)
        else:
            return self.quick_select(i+1, right, k)

    def findKthLargest(self, nums: list[int], k: int) -> int:
        self.nums = nums
        num = self.quick_select(0,len(self.nums)-1,k)
        return num


if __name__ == '__main__':
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    print(f"{nums,k}")
    print('----------Answer Below----------')
    print(Solution().findKthLargest(nums, k))
