# class Solution:
#     def quick_sort(self, left, right):
#         if left > right:
#             return
#         self.nums[left] = str(self.nums[left])
#         base = self.nums[left]
#         i, j = left, right
#         while i != j:
#             self.nums[i] = str(self.nums[i])
#             self.nums[j] = str(self.nums[j])
#             while int(self.nums[j][0]) <= int(base[0]) and i < j:
#                 j -= 1
#                 self.nums[j] = str(self.nums[j])
#             while int(self.nums[i][0]) >= int(base[0]) and i < j:
#                 i += 1
#                 self.nums[i] = str(self.nums[i])
#             if i < j:
#                 temp = self.nums[i]
#                 self.nums[i] = self.nums[j]
#                 self.nums[j] = temp
#         self.nums[left] = self.nums[i]
#         self.nums[i] = base
#         self.quick_sort(left, i-1)
#         self.quick_sort(i+1, right)

#     def largestNumber(self, nums: list[int]) -> str:
#         self.nums = nums
#         self.quick_sort(0, len(self.nums)-1)
#         return ''.join(self.nums)

class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num

if __name__ == '__main__':
    nums = [3, 30, 34, 5, 9]
    print(f"{nums}")
    print('----------Answer Below----------')
    print(Solution().largestNumber(nums))
