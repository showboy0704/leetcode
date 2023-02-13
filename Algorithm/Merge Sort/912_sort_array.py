class Solution:
    def mergesort(self, l, m, r):
        i = j = 0
        sort_list = []
        l1, l2 = self.nums[l:m], self.nums[m:r]
        while i < len(l1) and j < len(l2):
            if l1[i] <= l2[j]:
                sort_list.append(l1[i])
                i += 1
            else:
                sort_list.append(l2[j])
                j += 1
        if i == len(l1):
            sort_list.extend(l2[j:])
        elif j == len(l2):
            sort_list.extend(l1[i:])
        self.nums[l:r] = sort_list

    def sortArray(self, nums: list[int]) -> list[int]:
        self.nums = nums
        for power in range(17):
            size = 2**power
            if size > len(nums):
                break
            for left in range(0, len(nums), size*2):
                mid = left+size
                right = mid+size
                if mid < len(nums):
                    self.mergesort(left, mid, right)
        return self.nums


if __name__ == '__main__':
    nums = [5,1,1,2,0,0]
    print(f"{nums}")
    print('----------Answer Below----------')
    print(Solution().sortArray(nums))
